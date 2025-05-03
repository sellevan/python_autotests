import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '32439b552b0fbcddcdab6095bda25f05'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
body_create = {    
    "name": "ЭмоБойчик",
    "photo_id": 817
}
body_change = {
    "pokemon_id": "307432",
    "name": "ЭмоБой",
    "photo_id": 817
}
body_addpokeball = {
    "pokemon_id": "307432"
}

respons_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_creation.text)

respons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(respons_change.text)

respons_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(respons_addpokeball.text)




