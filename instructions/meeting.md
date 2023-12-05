# Meeting Notes

Go through this template in preparation for your meeting with the course staff member. We are not grading you on this template, just will help with questions and discussion. Please note, staff have the right to ask you to schedule a second meeting. The goal is to help you flesh out a reasonable project for this course, so make sure to use these meetings as a resource!

## Project Ideas
What are some ideas for your project? Why does that interest you?
* To make a telegram bot to organize discussions in a telegram group.
* Background: My friends and I often have discussions on how to invest in a group chat. We have two major problems:
  * Difficulty to keep track of information:
    * Group memebers contribute valuable information everyday in the chat group. But it's hard for memebers to remember everthing if we don't note down these informaiton. As time passes, we tend to forget most of them.
  * Free-rider problem:
  * Some people are actively sharing information in the group, but some are just consumers of info. Those who keeps providing new infomation will feel less incentived if we don't have any incentives or punishment to encourage sharing.
<br></br>

**use cases:**
1. track discussion content in the chat group 
    - get data: speaker, time, content(str)  **how to deal with image?** 
    - use special string (such as $, #) to add label as topic 
2. store discussion data in google spreadsheet 
3. discussion log stats 
    - speaker: how many messages sent in past 7 days? 
    - topic: how many messages under this topic in past 7 days? how many people mentioned this topic in past 7 days?
    - provide stats when asked by users 
4. auto reminder 
    - sent weekly contribution ranking in the group


## What are the big ideas?
How does this address some of the big learning ideas of 5001?
1. flowchart
2. functions
3. use a various kind of data structures, especially list and dictionary
4. read and write files
5. Loops

## Code Design Thoughts
Are you including classes or APIs, what about dictionaries? One of the worst things you can do is go into a project assuming you are going to 'hard' code everything (this happens often with text based games, then students get stuck). You don't have to know details yet, but you should think about separation of concerns, and how to divide up your code. 
* store discussion data -> dictionary
* telegram API
* google spreadsheet API (write and read data)
* different modules:
  * collect data from the group
  * write and read googlesheet
  * data analysis
  * telegram bot command management

## Resources Found
What are some resources you have found already or already have access to? (APIs, libraries, past assignments, etc)
* a guide of making telegrambot with python: https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/
* read & write data from googlesheets: https://www.youtube.com/watch?v=hyUw-koO2DA

## Timeline
Setup a general timeline that includes research and development, and when you want to have certain aspects of the project done.
* By Nov 22: project design, flowchat, code design, read API doc
* By Nov 30: finish core functions: collect data, read lable from message, write into googlesheet
* Dec 1 - 5: test, debug
* Dec 6: finish final project report, submit
