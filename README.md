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

Major use cases:
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

1. download:
* `folder` keys : contains Google sheet authentication json file. You can replace with your own authentication if you want to use your own Google sheet.
* main.py
* message_cleaner.py

2. install packages: \
Install the library for interaction with telegram bot
```python
pip install pyTelegramBotAPI
```
Install the library fo dealing with Google spreadsheet
```python
pip install gspread 
```
3. Run \
Run `main.py`. The function `BOT.infinity_polling()` will keep it running. When it is running, the bot is functioning. Once it stops, the bot won't work.


**A list of libaries used:**
* telebot (Interact with telegram, must install pyTelegramBotAPI first)
* gspread (Interact with Google spreadsheet, must install gspread first)
* json
* re
* datetime


**Use your own Google sheets** \
The bot is set to send data in this [sheet](https://docs.google.com/spreadsheets/d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit#gid=0). If you want to use your own Google sheet, please follow these steps:
1. Get your own Google authentication file \
Authentication is a json file you can generate and download from your Google account. The detail steps can be found [here](https://docs.gspread.org/en/v5.12.0/oauth2.html). Once you get your own authentication json file, put it inside the `keys` folder to replace the old one. When you generate the authentication file, you will also be given a client email address. Save this email address to be used later. (The client_email is default to be grace-bot@doc-writer-bot.iam.gserviceaccount.com).
2. Make your Google sheet accessible \
Create your own Google speadsheet and share it with your own client_email address. Make sure to give it "editor" role. \
Then open `main.py` and:
* change the value of the variable `CRE_PATH` to the file path of your own authentication json file path.
* change the value of the variable `FILE_NAME` to be the file name of your own Google spreadsheet
* change the value of the variable `SHEET_NAME` to be the sheet name of the sheet of your own Google spreadsheet you intended to write data
* change the value of the variable `FILE_URL` to be the url of your own Google spreadsheet so that the bot will direct to this file in help message.


**Use your own Bot** \
You can run the program using you own bot. Go to `@BotFather` in telegram to create a new bot and get your bot token. Then open `main.py` and change the value of the variable `BOT_TOKEN` to be your own token.


**References**
* [telegram bot API guide](https://core.telegram.org/bots/api#available-methods)
* [pyTelegramBotAPI library guide](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md#getting-started)
* [gspread guide](https://docs.gspread.org/en/v5.12.0/index.html)


## Code Review ?
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs ?
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing ?
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
