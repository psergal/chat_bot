import requests
# from dotenv import load_dotenv
# from os import getenv
import os
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
                bot.send_message(chat_id=telegram_chat_id, text=f'У вас проверили работу "{work_name}"\n{rezult_report}')
            elif json_resp['status'] == 'timeout':
                params.update({'timestamp': json_resp['timestamp_to_request']})
        except requests.exceptions.ReadTimeout as e:
            print(f'Catch the timeout error:  {e}')
        except requests.exceptions.ConnectionError as e:
            print(f'Catch the ConnectionError error:  {e}')


if __name__ == '__main__':
    # load_dotenv()
    # dvmn_token = getenv('DVMN_TOKEN')
    dvmn_token = os.environ['DVMN_TOKEN']
    # tlg_token = getenv('TLG_TOKEN')
    tlg_token = os.environ['TLG_TOKEN']
    # chat_id = getenv('TLG_CHAT_ID')
    chat_id = os.environ['TLG_CHAT_ID']
    check_devmn_lesson(dvmn_token, tlg_token, chat_id)
