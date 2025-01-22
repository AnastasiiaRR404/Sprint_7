
import json
import allure
import pytest
import requests

import test_data


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('Создание заказ c разными цветами скутера, BLACK, GREY или оба цвета'
                        'если цвет самоката не выбран, получим track')
    @pytest.mark.parametrize('color', [test_data.order_data_black_color, test_data.order_data_grey_color, test_data.order_data_two_colors, test_data.order_data_without_color])
    def test_create_order_with_different_selected_scooter_colors(self, color):
        payload_string = json.dumps(color)
        response = requests.post(url=f'{test_data.URL}/api/v1/orders', data=payload_string, headers=test_data.HEADERS)
        assert response.status_code == 201 and 'track' in response.json()
