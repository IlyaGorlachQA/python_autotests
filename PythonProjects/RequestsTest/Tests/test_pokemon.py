import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b2b1bde570ec45f6228af85e247e74f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '28847'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_id_response():
    response_id = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_id.json()['data'][0]['trainer_name'] == 'Gorinich'