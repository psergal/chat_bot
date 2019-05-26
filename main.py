from time import sleep
import requests
from dotenv import load_dotenv
import os
import http.client as httplib
import logging
from urllib.parse import urlparse


def devmn_api():
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    httplib.HTTPConnection.debuglevel = 0  # 1 -включает
    logging.basicConfig(filename='chat_bot.log', level=logging.DEBUG, format=log_format, filemode='w')
    logger = logging.getLogger("requests.packages.urllib3")
    logger.info(f'START {devmn_api.__name__}')

    load_dotenv()
    token = os.getenv('dvmn_token')
    headers = {
        'User-Agent': 'curl',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'Keep-Alive',
        'Authorization': token
    }
    while True:
        timestamp = 1.5565616562438638
        api = 'https://dvmn.org/api'
        paths = ['long_polling', 'user_reviews']
        # resp = requests.get(f'{api}/{paths[1]}/', headers=headers)
        resp = requests.get(f'{api}/{paths[0]}/?timestamp={timestamp}', headers=headers)
        for message in resp:
            logger.info(f'Devman response {message}')
            print(message)
            sleep(1)

    # https://dvmn.org/api/long_polling/?timestamp=1455609162


if __name__ == '__main__':
    devmn_api()