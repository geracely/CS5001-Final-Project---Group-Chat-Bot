"""
This program is used to clean message data.

Features:
* Format data, such as time, ID
* Extract keyword from message text

More functions may be added to further process message data.
"""

import re  # regular expression
import datetime

# default time format used to clean data
TIME_FORMAT = "%Y-%m-%d %H:%M"


def get_time(timestamp: int, time_format: str = TIME_FORMAT) -> str:
    """
    Convert timestamp to readable time format.
    If format is not given, default format will be used.
    Example:
        >>> get_time(1701988859)
        '2023-12-07 22:40'
        >>> get_time(1701988859, "%Y-%m-%d")
        '2023-12-07'

    Args:
        timestamp: a timestamp number
        time_format: use '%Y', '%m', '%d', '%H', '%M' to represent\
        year, month, date, hour, and minute respectively

    Returns:
        str: the formated time string
    """
    datetime_object = datetime.datetime.utcfromtimestamp(timestamp)
    return datetime_object.strftime(time_format)


def generate_id(chat_id: int, msg_id: int) -> str:
    """
    to generate a unique_id for every piece of message
    in the chat
    Example:
        >>> generate_id(-1002005006416, 69)
        '-1002005006416_69'

    Args:
        chat_id: id of a chat
        msg_id: id of a message in the chat

    Returns:
        str: combine chat_id and msg_id to form a unique id
    """
    return str(chat_id) + '_' + str(msg_id)


def get_username(first_name: str, last_name: str) -> str:
    """
    Concatenate first_name and last_name to be user_name
    Leave as blank if it's value is None
    Example:
       >>> get_username('Jerry', None)
       'Jerry'
       >>> get_username(None, None)
       ''
       >>> get_username('Alice', 'Potter')
       'Alice Potter'

    Args:
        first_name: user's first name
        last_name: user's last name

    Returns:
        str: full name of the user
    """
    return f"{first_name or ''} {last_name or ''}".strip()


def get_keyword(message_text: str, symbol: str) -> str:
    """
    Extract keyword from message text with special symbol\
    such as "$" or "#".
    Keyword contains strings after the symbol and\
    before the first whitespace afterward.
    keyword is formatted to all lower cases.
    Example:
        >>> get_keyword("check out $tsla Elon will launch a rocket.", "$")
        'tsla'
        >>> get_keyword("check out #tsla Elon will launch a rocket.", "#")
        'tsla'
        >>> get_keyword("check out Elon will launch a rocket.", "#")
        ''

    Args:
        message_text: long text from message
        symbol: special str marking the position of the keyword
    Returns:
        str: the clean keyword
    """
    pattern = re.escape(symbol) + r'(\S+)'
    match = re.search(pattern, message_text)
    if match:
        keyword = match.group(1)
    else:
        return ''

    return keyword.lower()
