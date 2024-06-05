import random
import string
import urls
import requests


def generate_payload_for_user():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_random_string(8)
    password = generate_random_string(8)
    name = generate_random_string(8)

    payload = {
        'email': f'{email}@yandex.ru',
        'password': password,
        'name': name
        }
    return payload


def generate_payload_for_order():
    response = requests.get(urls.BASE_URL + urls.INGREDIENTS_ENDPOINT)
    ingredients_list = response.json()['data']
    ingredients_bun = []
    ingredients_main = []
    ingredients_sauce = []
    ingredients = []

    for i in ingredients_list:
        if i['type'] == 'bun':
            ingredients_bun.append(i['_id'])

        elif i['type'] == 'main':
            ingredients_main.append(i['_id'])

        else:
            ingredients_sauce.append(i['_id'])

    ingredients.append(ingredients_bun[random.randint(0, len(ingredients_bun) - 1)])
    ingredients.append(ingredients_main[random.randint(0, len(ingredients_main) - 1)])
    ingredients.append(ingredients_sauce[random.randint(0, len(ingredients_sauce) - 1)])

    return ingredients
