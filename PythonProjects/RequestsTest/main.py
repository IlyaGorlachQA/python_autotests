import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7b2b1bde570ec45f6228af85e247e74f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
BODY_CREATE = {
    "name": "Tramontana",
    "photo_id": 33
}
BODY_CHANGE = {
    "pokemon_id": "291101",
    "name": "Koenigsegg",
    "photo_id": 11
}
BODY_ADD = {
    "pokemon_id": "291101"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response.text)
message = response.json()['message']
print(message)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.text)
message = response_change.json()['message']
print(message)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD)
print(response_add.text)