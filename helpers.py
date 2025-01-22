import json
import requests
import random
import string


class Helpers:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        return login_pass

    def get_courier_id(self):
        login_pass_id = []
        log_pass = self.register_new_courier_and_return_login_password()
        login_pass_id.append(log_pass[0])
        login_pass_id.append(log_pass[1])

        payload = {
            'login': log_pass[0],
            'password': log_pass[1]}
        payload_string = json.dumps(payload)
        response = requests.post(url=payload_string)
        login_pass_id.append(response.json()['id'])
        return login_pass_id
