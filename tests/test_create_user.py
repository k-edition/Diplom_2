from user_api import UserApi
from helper import ModifyData
import allure


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    def test_create_user_success(self, get_payload, remove_user):
        response = UserApi.create_user(get_payload)
        access_token = response.json()['accessToken']
        remove_user(access_token)

        assert response.status_code == 200 and get_payload['email'] in response.text

    @allure.title('Проверка ошибки при попытке создания пользователя, который уже зарегистрирован')
    def test_create_user_duplicate(self, get_payload, remove_user):
        response = UserApi.create_user(get_payload)
        response_duplicate = UserApi.create_user(get_payload)
        access_token = response.json()['accessToken']
        remove_user(access_token)

        assert response_duplicate.status_code == 403 and "User already exists" in response_duplicate.text

    @allure.title('Проверка ошибки при попытке создания пользователя c пустым email')
    def test_create_user_empty_email(self):
        mod_payload = ModifyData.modify_create_user_payload('email', '')
        response = UserApi.create_user(mod_payload)

        assert response.status_code == 403 and "Email, password and name are required fields" in response.text

    @allure.title('Проверка ошибки при попытке создания пользователя c пустым паролем')
    def test_create_user_empty_password(self):
        mod_payload = ModifyData.modify_create_user_payload('password', '')
        response = UserApi.create_user(mod_payload)

        assert response.status_code == 403 and "Email, password and name are required fields" in response.text

    @allure.title('Проверка ошибки при попытке создания пользователя c пустым именем')
    def test_create_user_empty_name(self):
        mod_payload = ModifyData.modify_create_user_payload('name', '')
        response = UserApi.create_user(mod_payload)

        assert response.status_code == 403 and "Email, password and name are required fields" in response.text
