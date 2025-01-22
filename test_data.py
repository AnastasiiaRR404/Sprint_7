URL = 'https://qa-scooter.praktikum-services.ru'
HEADERS = {"Content-type": "application/json"}

order_data_black_color = {
    "firstName": "Настя",
    "lastName": "Ро",
    "address": "ул. Приморская, д. 3",
    "metroStation": 4,
    "phone": "+7 999 123 12 13",
    "rentTime": 3,
    "deliveryDate": "2025-03-20",
    "comment": "Позвоните пожалуйста",
    "color": [
        "BLACK"
    ]
}

order_data_grey_color = {
    "firstName": "Иван",
    "lastName": "Сидорчук",
    "address": "ул. Ломоносовская, д. 13, кв. 125",
    "metroStation": 8,
    "phone": "8 911 343 34 65",
    "rentTime": 8,
    "deliveryDate": "2025-07-19",
    "comment": "",
    "color": [
        "GREY"
    ]
}

order_data_two_colors = {
    "firstName": "Лия",
    "lastName": "Спиридонова",
    "address": "пер. Мучной, д. 4",
    "metroStation": 13,
    "phone": "+7 999 543 54 56",
    "rentTime": 1,
    "deliveryDate": "2025-05-28",
    "comment": "Не звонить",
    "color": [
        "GREY", "BLACK"
    ]
}

order_data_without_color = {
    "firstName": "Ева",
    "lastName": "Кирова",
    "address": "ул. Плеханова, д. 23, кв. 192",
    "metroStation": 10,
    "phone": "+7 999 765 65 89",
    "rentTime": 5,
    "deliveryDate": "2025-03-17",
    "comment": "",
    "color": []
}