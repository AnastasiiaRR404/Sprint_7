import allure
import requests

import test_data


class TestGetOrdersList:

    @allure.title('Проверка получения списка заказов авторизованным курьером')
    @allure.description('Проверка получения кода 200 при получении списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(url=f'{test_data.URL}/api/v1/orders/?courierId=454127')
        assert response.status_code == 200 and response.json()['orders'] == []