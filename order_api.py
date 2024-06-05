import requests
import urls
import allure


class OrderApi:

    @staticmethod
    @allure.step("Отправка запроса POST на создание заказа")
    def create_order(payload_for_create_order, access_token):
        return requests.post(urls.BASE_URL + urls.ORDERS_ENDPOINT, json=payload_for_create_order,
                             headers={'Authorization': access_token})

    @staticmethod
    @allure.step("Отправка запроса GET на получение заказов конкретного пользователя")
    def get_user_orders(access_token):
        return requests.get(urls.BASE_URL + urls.ORDERS_ENDPOINT, headers={'Authorization': access_token})
