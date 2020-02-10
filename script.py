# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# ИМПОРТ МОДУЛЕЙ
# ------------------------------------------------------------------
import requests
import json
# ------------------------------------------------------------------
# # ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
# ------------------------------------------------------------------
session = requests.Session()
headers = {
    'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
}
logins = ['apple', 'microsoft', 'instagram'] # список/массив логинов
ids = ['5821462185', '524549267', '25025320'] # список/массив id
# ------------------------------------------------------------------
# # Username to ID
# ------------------------------------------------------------------
if len(logins) != 0:
    print('------------------')
    print('ID - аккаунтов')
    print('------------------')
    for i in range(len(logins)):
        response = session.get('https://instagram.com/'+logins[i]+'?__a=1', headers=headers)
        data = json.loads(response.text)
        id = data['graphql']['user']['id']
        print(id)
# ------------------------------------------------------------------
# # ID to Username
# ------------------------------------------------------------------
if len(ids) != 0:
    print('------------------')
    print('Username - аккаунтов')
    print('------------------')
    for i in range(len(ids)):
        response = session.get('https://i.instagram.com/api/v1/users/'+ids[i]+'/info/', headers=headers)
        data = json.loads(response.text)
        id = data['user']['username']
        print(id)
