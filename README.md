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

## References Used
* [telegram bot API guide](https://core.telegram.org/bots/api#available-methods)
* [pyTelegramBotAPI library guide](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md#getting-started)

## Guide
Keep the code running, and then you can use the bot in telegram. You can talk to the bot privately or use it in a group chat. It will record every text message from the chat and write it into a google spreadsheet. Major use cases:

1. Use default command to intereact with the bot \
Available commands: \
    /start - introduction of the bot
    /help - View this help message
    /history - view stored chat history
2. Send message to the bot privately
    It will 

The message data will be stored in the following format:

The default google sheet is set to be this: https://docs.google.com/spreadsheets/d/12lW7o4B2HAdmv56essp6jRa31WmLnDyjn65bGEnsQgE/edit#gid=0
If you want to use another google sheet, please check installation instruction about how to set up Google sheet authentication.


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.


**A list of libaries used:**
* telebot (Interact with telegram, must install pyTelegramBotAPI first)
* gspread (Interact with Google spreadsheet, must install gspread first)
* json
* re
* datetime


**Setup google sheets API**
1. install the gspread library


client_email: grace-bot@doc-writer-bot.iam.gserviceaccount.com


* pyTelegramBotAPI library for handling Telegram messages
* gspread library for interacting with Google Sheets.


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
