# Telegram ChatBot that notifies when Devman's code review has been done 
***
## Introduction
This immature module can do a little. 
It polls [Devman API](https://dvmn.org/api/docs/) with Long Polling. 
If the code review is complete the Telegram BOT will send a message to the user.     


## Installing locally
You can install or upgrade python-telegram-bot with:  
 `$pip install requirements.txt`  
A student has to be sign up on the https://dvmn.org/ and has to send at least one lesson on the teacher side.
The student should acquire a token for working with API on the page with [Devman API](https://dvmn.org/api/docs/)
The student has to create his Bot following by this [instructions: how-do-i-create-a-bot](https://core.telegram.org/bots/faq#how-do-i-create-a-bot).
The student has to get chat_id which equal to user Id from the special Bot _@userinfobot_.
There are four setting for the proper work which has to be set on via `.env` file:
* `DVMN_TOKEN`
* `TLG_TOKEN`
* `HTTPS_PROXY`
* `TLG_CHAT_ID`   
Uncomment lines from the comment `for local debugging` and comment lines with `os.environ`     

## Getting started locally
Put this string to the command line  `python main.py` it launches loop with long poll requests.
The shortest way to try is when you send a trial lesson to the teacher code review by this link:
[rotating-planet](https://dvmn.org/modules/meeting-python/lesson/rotating-planet/#review-tabs) and then brings it back from the check. You will see print and Bot send you a message depends on review result.

## Deploying onto remote server (Heroku)
### Registration
* [Sign up](https://signup.heroku.com/login) by this link.
* Create your own repo on [Github](https://github.com/).
* Link your repo with your application.
* Your repo has to have `procfile` more information [there](https://devcenter.heroku.com/articles/procfile).
 It has to comprise this line `bot: python3 yourfilename.py`
  



## Project Goals
The code has been written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/modules/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/psergal/bitly/blob/master/license.md) file for details  

 

