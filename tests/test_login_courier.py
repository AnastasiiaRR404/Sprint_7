import json
import allure
import pytest
import requests
import test_data
from helpers import Helpers


class TestCourierCreate:

    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_login_successful(self):
        helper = Helpers()
        user = helper.register_new_courier_and_return_login_password()
        payload = {
            'login': user[0],
            'password': user[1]}
        payload_string = json.dumps(payload)
        response = requests.post(url=f'{test_data.URL}/api/v1/courier/login', data=payload_string, headers=test_data.HEADERS)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Проверка авторизации с невалидными данными')
    @allure.description('Для проверки, были введены не валидные логин и пароль'
                        'если логин/пароль не верный, вернется ошибка'
                        ' если залогинеться несуществующим пользователем в  базе, вернется ошибка')
    @pytest.mark.parametrize(
        'login,password, code, error',
        [
            ['881f9914-e73d-4a66-8f76-0eacaa4424e6', 'e853534f-d621-4e53-8a21-c6caad4205a1', 404, 'Учетная запись не найдена'],
            ['siananananna', '', 400, 'Недостаточно данных для входа'],
            ['', '12345dskfcdssd', 400, 'Недостаточно данных для входа'],
            ['siananananna', '12345dskfcdssd', 404, 'Учетная запись не найдена']
        ]
    )
    def test_courier_login_not_successful(self, login, password, code, error):
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        response = requests.post(url=f'{test_data.URL}/api/v1/courier/login', data=payload_string, headers=test_data.HEADERS)
        assert response.status_code == code and error in response.text