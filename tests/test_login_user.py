from user_api import UserApi
import data
import allure


class TestLoginUser:
    @allure.title('Проверка авторизации под логином существующего пользователя')
    def test_login_real_user(self, default_user):
        login_response = UserApi.login_user(default_user)

        assert login_response.status_code == 200 and login_response.json()['user']['email'] == default_user['email']

    @allure.title('Проверка ошибки при попытке авторизации пользователя c неверным логином')
    def test_login_user_with_invalid_login(self, default_user):
        invalid_login = default_user['email'][1:]
        default_user['email'] = invalid_login
        login_response = UserApi.login_user(default_user)

        assert login_response.status_code == 401 and data.text[401][0] in login_response.text

    @allure.title('Проверка ошибки при попытке авторизации пользователя c неверным паролем')
    def test_login_user_with_invalid_password(self, default_user):
        invalid_password = default_user['password'][1:]
        default_user['password'] = invalid_password
        login_response = UserApi.login_user(default_user)

        assert login_response.status_code == 401 and data.text[401][0] in login_response.text
