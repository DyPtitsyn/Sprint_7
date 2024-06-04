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

class ModifyData:
    @staticmethod
    def modify_create_courier_body(key, value):
        body = generate_payload_for_create_courier().copy()
        body[key] = value

        return body

    @staticmethod
    def modify_login_courier_body(body, key, value):
        new_body = body.copy()
        new_body[key] = value
        return new_body

    @staticmethod
    def modify_payload_for_login_courier(body):
        new_body = body.copy()
        del new_body["firstName"]
        return new_body

    @staticmethod
    def modify_create_order_body(key, value):
        body = generate_payload_for_create_order().copy()
        body[key] = value
        return body
