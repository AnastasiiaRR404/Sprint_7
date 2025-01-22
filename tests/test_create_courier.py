import json
import requests
import allure
import pytest
import test_data
from helpers import Helpers
import utils


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

        response_id = requests.post(f'{utils.BASE_URL}/courier/login', data=payload_string, headers=test_data.HEADERS)
        courier_id = response_id.json()['id']
        utils.delete_courier(courier_id)

    @allure.title('Проверка создания курьера с невалидными данными')
    @allure.description('если login/password/firstName не верный, вернется ошибка'
                        ' если попробовать создать уже существующего пользователем в  базе, вернется ошибка')
    @pytest.mark.parametrize(
        'login,password, code, error',
        [
            ['siana04', '12345', 409, 'Этот логин уже используется. Попробуйте другой.'],
            ['siana04', '', 400,'Недостаточно данных для создания учетной записи'],
            ['', '12345', 400, 'Недостаточно данных для создания учетной записи']
        ]
    )
    def test_courier_create_not_successful(self, login, password, code, error):
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        response = requests.post(url=f'{test_data.URL}/api/v1/courier', data=payload_string, headers=test_data.HEADERS)
        assert response.status_code == code and error in response.json()['message']
