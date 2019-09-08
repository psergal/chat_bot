# Telegram Chat Bot that notify when Devman's code review has been done 
***
## Introduction
This immature module can do little   
It polls [Devman API](https://dvmn.org/api/docs/) with long poll
If the code review is complete the Telegram BOT will send a message to the user     


## Installing
You can install or upgrade python-telegram-bot with:  
 `$pip install requirements.txt`  
Student has to be registered on the https://dvmn.org/  
and has at least one lesson on the teacher side  
Student should acquire a token on the page with [API](https://dvmn.org/api/docs/)  
and use it in a header by putting it into `.env` file with name `DVMN_TOKEN`   
Student has to create his own Bot following by this
 [instructions](https://core.telegram.org/bots/faq#how-do-i-create-a-bot)     
Student has to get chat_id which equal to user Id from the special Bot _@userinfobot_
and put it to the __ifnaime__ part of `main.py`  
If you have to use proxy to access the telegram  
create a _HTTPS_PROXY_ variable the `.env`  with `socks5` prefix 

## Getting started
`python main.py`
The short way to try is when you send trial lesson to the teacher code review by this link:  
[rotating-planet](https://dvmn.org/modules/meeting-python/lesson/rotating-planet/#review-tabs)  
and bring it back from the check
You will see print and Bot send you a message depends on review result  

## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/modules/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/psergal/bitly/blob/master/license.md) file for details  
