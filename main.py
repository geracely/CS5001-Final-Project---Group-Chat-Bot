"""
The main driver for the bot

features:
interaction with telegram bot API
interaction with Google spreadsheet API
deal with bot commands
"""

import telebot  # library to interact with telegram
import gspread  # library to interact with Google spreadsheet
import json

from message_cleaner import get_time, generate_id, get_username, get_keyword

# get bot token from telegram @botfather
BOT_TOKEN = "5832009482:AAFTnzYLmBrdv1SOmpmc_76O8MhYQEF1CMU"
# create a bot instance and pass the bot token to it
BOT = telebot.TeleBot(BOT_TOKEN)
# chat types the bot intents to serve
CHAT_TYPES = ['private', 'group', 'supergroup']
# content types the bot intents to serve
CONTENT_TYPES = ['text']

# save Google sheet credential to a json file
CRE_PATH = 'keys/doc-writer-bot-2ecdd25ee805.json'
MAX_COLUMNS = 5  # Maximum columns allowed to be written in one call

# manually create the sheet in the authorized Google account
# the sheet must be shared with the email linked to the credential account
FILE_URL = ('https://docs.google.com/spreadsheets/\
d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit?usp=sharing')
FILE_NAME = 'chat_history_from_bot'
SHEET_MSG = 'all_messages'  # name of the sheet to store message raw data

# bot commands
START = 'start'
HELP = 'help'
HISTORY = 'history'

# messages send to users
HELP_MSG = """
    Available commands:
    /start - introduction of the bot
    /help - View this help message
    /history - view stored chat history
    """
START_MSG = f"""
Welcome! I am your chat assistant.\
Start using by inviting me to your group chat \
or send messages directly to me.
I can record every chat message from you or your group.
Chat history can be found in this google sheet:{FILE_URL}
"""
HISTORY_MSG = f"Chat history:{FILE_URL}"


@BOT.message_handler(commands=[START, HELP, HISTORY],
                     func=lambda message: message.chat.type in CHAT_TYPES)
def reply_msg(command) -> None:
    """
    when user give command, reply corresponding guidance to users

    Args:
        command: bot command from users
    Returns:
        None
    """
    if command.text.startswith(f'/{START}'):
        BOT.reply_to(command, START_MSG)
    elif command.text.startswith(f'/{HELP}'):
        BOT.reply_to(command, HELP_MSG)
    elif command.text.startswith(f'/{HISTORY}'):
        BOT.reply_to(command, HISTORY_MSG)


def write_spreadsheet(chat_message: list, file_name: str,
                      sheet_name: str) -> None:
    """
    Write message data in Google spreadsheet. One list is for one row.
    The order of the list represents order of columns of the sheet.
    The append_row function only allows no more than five columns for each \
    call. Therefore, the chat_message list cannot have more than five elements.

    Args:
        chat_message:
        file_name:
        sheet_name:
    Returns:
        None
    """
    # set up the credential
    cre = gspread.service_account(filename=CRE_PATH)
    file = cre.open(file_name)
    sheet = file.worksheet(sheet_name)

    if len(chat_message) > MAX_COLUMNS:
        raise ValueError(f"chat_message has more than {MAX_COLUMNS} elements, "
                         f"which exceeds the maximum allowed.")
    else:
        sheet.append_row(chat_message)


# get message from chat
@BOT.message_handler(func=lambda message: True,
                     content_types=CONTENT_TYPES, chat_types=CHAT_TYPES)
def get_chat_message(message) -> None:
    """
    Get chat message from telegram and then push to Google Spreadsheet.
    Message is a special type defined by the class.
    To simplify the process, each message is being fetched and then pushed.
    Therefore, each chat_message list will be one row.
    The chat_message list cannot have more than five elements as required\
    by the write_spreadsheet() function.
    The structure of the list is set to be:
    [msg_time, user_name, ticker, text, msg_details]
    Msg_details is a json string to store extra data of the message.

    Args:
    message: Provided by telegram API. Contains All data in a chat message.

    Returns:
        None
    """

    #  load main part of the message data
    msg_time = get_time(message.date)
    user_name = get_username(message.from_user.first_name,
                             message.from_user.last_name)
    ticker = get_keyword(message.text, '$')
    text = message.text

    #  put extra data into one dict
    msg_detail = dict(
        topic=get_keyword(message.text, '#'),
        user_id=message.from_user.username,
        chat_id=message.chat.id,
        chat_type=message.chat.type,
        chat_name=message.chat.title,
        reply_to=generate_id(message.chat.id,
                             message.reply_to_message.message_id)
        if message.reply_to_message else None,
        unique_id=generate_id(message.chat.id, message.id)
    )

    #  put all data into a list to be inserted to the spreadsheet
    #  Five columns maximum to be written in a single operation
    chat_message = [
        msg_time,
        user_name,
        ticker,
        text,
        json.dumps(msg_detail)
    ]

    #  send to spreadsheet only when it's from real user and not a command
    if (message.from_user
            and message.from_user.is_bot is False
            and text.startswith('/') is False):
        write_spreadsheet(chat_message, FILE_NAME, SHEET_MSG)
        print(f'[message recorded] {user_name}: {message.text}.')


print('bot starts running...')
print('Start send message in the chat group or to the bot privately.')
print(f'The bot will record your message in file: {FILE_URL}.')
BOT.infinity_polling()
print('bot stops running.')
