import json
import requests
import allure
import pytest
import test_data
from helpers import Helpers


class TestCourierCreate:

    @allure.title('Проверка успешного создания курьера')
    def test_courier_create_successful(self):
        helper = Helpers()
        login = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        response = requests.post(url=f'{test_data.URL}/api/v1/courier', data=payload_string,
                                 headers=test_data.HEADERS)
        assert response.status_code == 201 and '{"ok":true}' == response.text

    @allure.title('Проверка создания курьера с невалидными данными')
    @allure.description('если login/password/firstName не верный, вернется ошибка'
                        ' если попробовать создать уже существующего пользователем в  базе, вернется ошибка')
    @pytest.mark.parametrize(
        'login,password, error',
        [
            ['siana04', '12345', 409],
            ['siana04', '', 400],
            ['', '12345', 400]
        ]
    )
    def test_courier_create_not_successful(self, login, password, error):
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        response = requests.post(url=f'{test_data.URL}/api/v1/courier', data=payload_string, headers=test_data.HEADERS)
        assert response.status_code == error