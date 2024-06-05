import requests
import urls
import allure


class UserApi:

    @staticmethod
    @allure.step("Отправка запроса POST на создание пользователя")
    def create_user(payload_for_create_user):
        return requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=payload_for_create_user)

    @staticmethod
    @allure.step("Отправка запроса DELETE на удаление пользователя")
    def delete_user(access_token):
        return requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': access_token})

    @staticmethod
    @allure.step("Отправка запроса POST на авторизацию пользователя")
    def login_user(payload_for_login_user):
        return requests.post(urls.BASE_URL + urls.LOGIN_USER_ENDPOINT, json=payload_for_login_user)

    @staticmethod
    @allure.step("Отправка запроса PATCH на изменение данных пользователя")
    def change_user_info(update_payload, access_token):
        return requests.patch(urls.BASE_URL + urls.CHANGE_USER_INFO_ENDPOINT, json=update_payload,
                              headers={'Authorization': access_token})
