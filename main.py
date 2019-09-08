import requests
from dotenv import load_dotenv
from os import getenv
import telegram.ext


def check_devmn_lesson(devman_token, telegram_token, telegram_chat_id):
    bot = telegram.Bot(telegram_token)

    headers = {
        'User-Agent': 'curl',
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'Keep-Alive',
        'Authorization': devman_token
    }
    timestamp = 0
    api = 'https://dvmn.org/api'
    resp = requests.get(f'{api}/long_polling/', headers=headers)
    resp.raise_for_status()
    json_resp = resp.json()
    print(json_resp.get('timestamp_to_request'))
    while True:
        if json_resp['status'] == 'found':
            timestamp = json_resp['last_attempt_timestamp']
            print(json_resp['status'], json_resp['request_query'])
            print(json_resp['new_attempts'])
            work_name = json_resp['new_attempts'][0]['lesson_title']
            work_done = json_resp['new_attempts'][0]['is_negative']
            rezult_report = 'К сожалению в работе нашлись ошибки' if work_done \
                else 'Работа принята, можно приступать к слледующему уроку'
            bot.send_message(chat_id=telegram_chat_id, text=f'У вас проверили работу "{work_name}"')
            bot.send_message(chat_id=telegram_chat_id, text= rezult_report)
        elif json_resp['status'] == 'timeout':
            timestamp = json_resp['timestamp_to_request']
            print(json_resp['status'], json_resp['request_query'])
        try:
            resp = requests.get(f'{api}/long_polling/?timestamp={timestamp}', headers=headers)
            resp.raise_for_status()
            json_resp = resp.json()
        except requests.exceptions.ReadTimeout as e:
            print(f'Catch the timeout error:  {e}')
        except requests.exceptions.ConnectionError as e:
            print(f'Catch the ConnectionError error:  {e}')


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = getenv('DVMN_TOKEN')
    tlg_token = getenv('TLG_TOKEN')
    chat_id = '709528889'
    check_devmn_lesson(dvmn_token, tlg_token, chat_id)
