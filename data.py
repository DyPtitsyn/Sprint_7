import random
import string


def generate_payload_for_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def generate_payload_for_create_order():
    payload = {
        "firstName": "Dima",
        "lastName": "Gromov",
        "address": "221b Baker street, London",
        "metroStation": 8,
        "phone": "+7 888 777 66 55",
        "rentTime": 5,
        "deliveryDate": "2024-07-01",
        "comment": "elementary",
        "color": ["BLACK"]
    }
    return payload
