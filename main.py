import requests
import os
import telegram.ext
import logging

# for local debugging
# from dotenv import load_dotenv
# from os import getenv
# import sys

class TelegramLogsHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        tlg_token = os.environ['TLG_TOKEN']
        chat_id = os.environ['TLG_CHAT_ID']
        self.telegram_bot = telegram.Bot(tlg_token)
        self.telegram_bot.send_message(chat_id=chat_id, text='bot has started')

    def emit(self, record):
        log_entry = self.format(record)
        self.telegram_bot.send_message(chat_id=chat_id, text=f'{log_entry}')


def check_devmn_lesson(devman_token, telegram_token, telegram_chat_id):
    log_format = "%(levelname)s %(asctime)s - %(funcName)s - %(message)s"
    logger = logging.getLogger("__name__")
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    tlg_handler = TelegramLogsHandler()
    tlg_handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(tlg_handler)
    logger.setLevel(logging.INFO)

    headers = {
        'User-Agent': 'curl',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'Keep-Alive',
        'Authorization': devman_token
    }
    timestamp = None
    api = 'https://dvmn.org/api/long_polling/'
    params = {'timestamp': timestamp}
    while True:
        try:
            resp = requests.get(api, params=params, headers=headers)
            resp.raise_for_status()
            json_resp = resp.json()
            if json_resp['status'] == 'found':
                params.update({'timestamp': json_resp['last_attempt_timestamp']})
                work_name = json_resp['new_attempts'][0]['lesson_title']
                work_done = json_resp['new_attempts'][0]['is_negative']
                rezult_report = 'К сожалению в работе нашлись ошибки' if work_done \
                    else 'Работа принята, можно приступать к слледующему уроку'
                logger.warning(f'У вас проверили работу "{work_name}"\n{rezult_report}')
            elif json_resp['status'] == 'timeout':
                params.update({'timestamp': json_resp['timestamp_to_request']})
        except requests.exceptions.ReadTimeout as e:
            logger.error(f'Catch the timeout error:  {e}', exc_info=True)
        except requests.exceptions.ConnectionError as e:
            logger.error(f'Catch the ConnectionError error:  {e}', exc_info=True)


if __name__ == '__main__':
    # for local debugging
    # load_dotenv()
    # dvmn_token = getenv('DVMN_TOKEN')
    # tlg_token = getenv('TLG_TOKEN')
    # chat_id = getenv('TLG_CHAT_ID')

    dvmn_token = os.environ['DVMN_TOKEN']
    tlg_token = os.environ['TLG_TOKEN']
    chat_id = os.environ['TLG_CHAT_ID']
    check_devmn_lesson(dvmn_token, tlg_token, chat_id)
