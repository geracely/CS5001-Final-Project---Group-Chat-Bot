# Final Project Report

* Student Name: Ye Li
* Github Username: geracely
* Semester: 2023 Fall
* Course: CS5001



## Description 
My friends and I often have discussions on investment in telegram group chat, such as a promising stock to pay attention to or a big news that could lead to a future major trend. But we are facing two major challenges to keep this chat group active and effective:
1. keep good track of valuable information:
New information is shared everyday in the group. But it's impossible for anyone to remember everthing without taking detailed notes. We need a tool to help us note down every piece of information and stored with a structured format, making it possible for us to revisit and reorganize these information to generate new knowledge.
2. free-rider problem:
Some people rarely add to the chat, even though most people in the group are constantly sharing information. We need to make rules that will reward people who contribute a lot and punish people who don't. But before we can put these rules into place, we need to be able to make clear data about what everyone has done.

Therefore, the goal of this project is to make a telegram bot as an helper in the group chat by keeping track of the chart history, giving each member's participation score, and even enforcing group rules (like kicking out members who aren't active for a certain number of days).


## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 
* get message from telegram chat (both private and group)
* Extract message text: time, from_user, ticker mentioned in text, full content of the message, and other extra info.
* write data into a google spreadsheet


## Guide
Keep the code running, and then you can use the bot in telegram. You can talk to the bot privately or use it in a group chat. It will record every text message from the chat and write it into a google spreadsheet. search `@graceread_bot` in telegram to find the bot. 

**Major use cases:**
1. Use default command to intereact with the bot \
Available commands: \
    /start - introduction of the bot \
    /help - View this help message \
    /history - view stored chat history
2. Send message to the bot privately or in a chat group having the bot (bot must be given admin role in the group) 
    * The bot will fetch every message sent by users and write the message into a Google spreadsheet
    * The spreadsheet has five columns: msg_time, user_name, ticker, text, msg_details
    * You can mention a stock using the format "$ticker" in the message so that the bot will put ticker name in the "ticker" column in the sheet
    * You can label your message under a specific topic using the format "#topic" in the message and the bot will put a "topic" label for the message under msg_details
    * The data in the spreadsheet can be further processed to produce stats of users, tickers, and topics

**Note:** \
The default google sheet is set to be this: https://docs.google.com/spreadsheets/d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit#gid=0
If you want to use another google sheet, please check installation instruction about how to set up Google sheet authentication.


## Installation Instructions 
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

**1. Clone files**
Git clone this repository: https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot \
The major files are:
* keys : a folder contains Google sheet authentication. Must be used with main.py
* main.py : the main driver of the program
* message_cleaner.py : must be used with main.py

**2. Install packages** \
Run `pip install -r requirements.txt`, or install respectively as below: \
Install the library for interaction with telegram bot
```python
pip install pyTelegramBotAPI
```
Install the library fo dealing with Google spreadsheet
```python
pip install gspread 
```
**3. Setup the bot in telegram Chat Group**
Create a chat group in telegram. Invite bot `@graceread_bot` to your chat group. The bot must be given `Admin` role in the group. \
You can also test the bot by directly send messages to it.

**4. Run bot** \
Run `python3 main.py`. \
Then you can:
* use bot command. Send `/help` to check for available commands.
* send any messages in the chat. The bot will record it into a Google spreadsheet.
<br />


### A list of libaries used:
* telebot (Interact with telegram, must install pyTelegramBotAPI first)
* gspread (Interact with Google spreadsheet, must install gspread first)
* json
* re
* datetime

### Use your own Google sheets
The bot is set to send data in this [sheet](https://docs.google.com/spreadsheets/d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit#gid=0). If you want to use your own Google sheet, please follow these steps:
1. Get your own Google authentication file \
Authentication is a json file you can generate and download from your Google account. The detail steps can be found [here](https://docs.gspread.org/en/v5.12.0/oauth2.html). Once you get your own authentication json file, put it inside the `keys` folder to replace the old one. When you generate the authentication file, you will also be given a client email address. Save this email address to be used later. 
2. Make your Google sheet accessible \
Create your own Google speadsheet and share it with your own client_email address. Make sure to give it "editor" role. \
Then open `main.py` and:
* change the value of the variable `CRE_PATH` to the file path of your own authentication json file path.
* change the value of the variable `FILE_NAME` to be the file name of your own Google spreadsheet
* change the value of the variable `SHEET_NAME` to be the sheet name of the sheet of your own Google spreadsheet you intended to write data
* change the value of the variable `FILE_URL` to be the url of your own Google spreadsheet so that the bot will direct to this file in help message.

### Use your own Bot
You can run the program using you own bot. Go to `@BotFather` in telegram to create a new bot and get your bot token. Then open `main.py` and change the value of the variable `BOT_TOKEN` to be your own token.
<br />


### References
* [telegram bot API guide](https://core.telegram.org/bots/api#available-methods)
* [pyTelegramBotAPI library guide](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md#getting-started)
* [gspread guide](https://docs.gspread.org/en/v5.12.0/index.html)
<br />

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 
<br> <br />
The `main.py` is the main driver for the program. It handles all the interactions with telegram bot API and Google spreadsheet API. 
<br> <br />
The `reply_msg()` is in charge of all the automatic replies to commands that require a reply. And for each command, specific reply message should be given accordingly. Currently, only three commands require a reply. More can be added when necessary in the future. 
```python
@BOT.message_handler(commands=[START, HELP, HISTORY],
                     func=lambda message: message.chat.type in CHAT_TYPES)
def reply_msg(command) -> None:
    if command.text.startswith(f'/{START}'):
        BOT.reply_to(command, START_MSG)
    elif command.text.startswith(f'/{HELP}'):
        BOT.reply_to(command, HELP_MSG)
    elif command.text.startswith(f'/{HISTORY}'):
        BOT.reply_to(command, HISTORY_MSG)
```

The `write_spreadsheet` is used to write data into Google spreadsheet. The file must be open with credential. The Credential file can be downloaded from Google (see details in Installation). Notice that Google has a limitation of items to be wrote in one call, so the length of the `chat_message` list cannot exit the maximum number.
```python
def write_spreadsheet(chat_message: list, file_name: str,
                      sheet_name: str) -> None:
    cre = gspread.service_account(filename=CRE_PATH)
    file = cre.open(file_name)
    sheet = file.worksheet(sheet_name)

if len(chat_message) > MAX_COLUMNS:
    raise ValueError(f"chat_message has more than {MAX_COLUMNS} elements, "
                     f"which exceeds the maximum allowed.")
    else:
        sheet.append_row(chat_message)
```

The `get_chat_message()` function is used to fetch messages from telegram API. Since we will directly write each piece of message to Google sheet once we get data from telegram, we do the data formating process together with the get message process. `message` is a special object defined by the `message` class.
```python
@BOT.message_handler(func=lambda message: True,
                     content_types=CONTENT_TYPES, chat_types=CHAT_TYPES)
def get_chat_message(message) -> None:
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
```

Normally, this program should be deployed to a cloud server so that to keep the bot running. Since we don't do deployment in the project yet, we use the infinity_polling() method to keep it running use our local machine. The process is to continuously poll the Telegram servers for new updates, allowing the bot to react to messages, commands, and other events in real-time.
```python
BOT.infinity_polling()
```

The file `message_cleaner.py` is used to format message data. Four functions `get_time, generate_id, get_username, get_keyword` are designed to process time format, generate an unique id for each message, generate user full name, and to extract keywords from message text. `get_keyword` can find the keyword in a message text by recognizing specific pattern. First, we defined the pattern as special symbol + keyword + whitespace. We can then find the keyword by locate the special symbol first and then extract the first set of non-whitespaced strings after it. We use regular expression to represent the pattern.
```python
def get_keyword(message_text: str, symbol: str) -> str:
    pattern = re.escape(symbol) + r'(\S+)'
    match = re.search(pattern, message_text)
    if match:
        keyword = match.group(1)
    else:
        return ''

    return keyword.lower()

```


### Major Challenges
1. link to telegram bot \
Though there is pyTelegramBotAPI as a very useful tool to assist interaction with telegram, I still face big chanllenges when trying to access telegram bot and use its data. At first, I set up the bot quickly with private chat, but I just can't make it with group chat. The bot stopped responding once I invited it into a group chat. I searched telegram bot API docs and tried everything it tells me, but it just didn't work. After reading the doc of pyTelegramBotAPI, I found that they have a telegram group for developers to communicate with each other. So I joined the group and asked about my problem. People are very friendly in that group and quickly offered my many advices. Some of them asked me about the type of my chat group. Is it a supergroup? I said no, because I think I just create a normal group not something special. But a person told me that just set the condition as `chat_types in ['group', 'supergroup']`. I tried and the problem immediately fixed! It turns out that telegram forms a supergroup by default.

2. Write data to Google spreadsheet \
My original plan is to unfold all the message data into columns and then write to Google spreadsheet, so that it will be very convenient for me to reuse those data on Google spreadsheet. But when I test the program, the data wrote in the sheet always missing some items. At first, I thought it's because of the order of the insertion process of Google's API. So I tried to specify every item in the message list and enforce the append() method to follow my order. Then it turns out that they only allow five items to be processed for one call. So if I want to append a row with data having more than five columns, it will be very complicated. So I re-designed the data structure of my message data and put most of extra data into a json. This also means that I need to add more features in the future if I want to further process those data.

3. The collaboration of get_message and write_spreadsheet \
I think about this task flow for a long time. At first, I designed a dict to carry all the message data. I thought that I can then convert the dict into lists and then insert those lists as rows into the spreadsheet. But then I found myself in big trouble because it's hard to find a way to arrange the order of these two actions. When and where is the cut point to move the data to spreadsheet? And how can I avoid writing data with repetion? In the end, I decided to solve it in the simplist way to process those messages piece by piece.  Every time, a piece of message is being posted in the chat, the program will fetch the message and format it (a list ready to be a row), and then write it as a row in the spreadsheet imediately. In this way, I don't need the convert dict to list process anymore, and I don't have to worry about how to deal with data batches. But one big disadvantage of this design is that some messages might be missed if new messages emerge very fast. But this may not be a big problem because I can enable slow mode in telegram chat group. 


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc) 

The project has two main features. 
1. To make a telegram bot that can interact with commands sent through telegram. The result is demonstrated in this video [example_runs_command](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/example_run_command.mov), where I tested all three commands with the bot (`/start`, `/help`,`/history`).
2. To let the bot record the message send in telegram chat and then write into a Google spreadsheet. The result is demonstrated in this video [example_runs_command](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/example_run_send_message.mov). In the video, I tried to send different messages in the telegram chat group, and you will see the messages are written into a Google spreadsheet line by line in a specific format. I also tested a message with special symbol "$" in it. The expected result is to get the keyword after '$' and to put it in the 'ticker' column of the Google spreadsheet.

This google [spreadsheet](https://docs.google.com/spreadsheets/d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit?usp=sharing) is a demonstration of all the messages recorded by the bot.


## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

### Test message_cleaner.py
A unit test is performed by `test_message_cleaner.py`. Test result can be found in the file [test_result](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_result.txt)

### Test main.py
Tested through interaction with telegram while running. 
1. Test reply_message(command) \
1.1 Try the three commands inside telegram and to see whether we get expected results. The following pics show the result when type commands: `/start`, `/help`, `/history`. The bot replied to each command as expected.
![test /start](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_command_start.png)
![test /help](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_command_help.png)
![test /history](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_command_history.png)

1.2 Test with false commands. When we enter commands other than `/start`, `/help`, `/history`, we expect it to be reply nothing. And, this message should NOT be written into the Google sheet. As shown in the pic below, when type the command `/happy`, the bot reply nothing, and that message is not being recorded in Google sheet.
![test wrong command](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_wrong_command.jpg)

2. Test write_spreadsheet(message)
I add one more item in the message list and run the program again. An ValueError is given in coonsole as expected. Full results can be found in the file [test_result](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_result.txt)
```python
ValueError: chat_message has more than 5 elements, which exceeds the maximum allowed.
```

3. Test get_message()
This function is supposed to get message from telegram chat and then write into Google sheet via valling the function write_spreadsheet(message). I test it by sending messages in telegram and then check if those messages are send to Googlesheet. If sent, print out the message in the console. Results in the console can be found in the file [test_result](https://github.com/geracely/CS5001-Final-Project---Group-Chat-Bot/blob/main/example_runs%26testing/test_result.txt). 



## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. \
**Deployment** \
To deploy the program on a cloud server so I can really put this bot in use.
**Support more data types** \
* Add special support for Chinese characters (the get_keywords() function has some flaws when dealing with Chinese characters)
* Add support to images (now only support text message)
**Message summaries** \
* produce stats based on message data collected
* send summaries to chat group weekly or triggered by bot command
**Manage groups** \
Make this bot to do managing tasks for the chat group, such as add new memebers, kick out memebers based on rules, pin important messages, etc.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
<br />
I enjoyed learning this course in general. This course is not very in-depth but complete enough to cover most of important topics in python programming. I feel this would be really helpful to set a foundation for my future learning. The major learning points for me are: 
* How to break-down big problem into small simple functions and then to assemble everything up to solve the problem
* Different data types especially advanced types such as set, list, and dict that offer great flexibility for storing and processing data
* Learned about class and how to use them. In my final project, I used an external libary and relied heavily on class designed by others. I was a bit of confused about the purpose of class. But after I've done the final project, I can see that class can offer great help especially for collaberation.

The experience of doing final project makes me realize that I need a good understanding on class&objects and stacks&queues if I want to do real projects because real projects often involve collaberation and dealing with task flows. I also enjoyed the process of learning by doing. Many vague concepts become much more clearer to me after I did my own project.I plan to use python as much as possible to solve my own real-life problems to assist my learning process in the future.




