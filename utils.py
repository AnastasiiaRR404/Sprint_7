import requests


BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'


def delete_courier(courier_id):
    response = requests.delete(f'{BASE_URL}/courier/{courier_id}')
    return response.status_code == 200