from user_api import UserApi
import data
import allure


class TestChangeUserInfo:

    @allure.title('Проверка изменения логина авторизованного пользователя')
    def test_change_login_user_authorized(self, default_user):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        update_login = default_user['email'][1:]
        update_payload = {'email': update_login}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 200 and update_response.json()['user']['email'] == update_login

    @allure.title('Проверка изменения логина неавторизованного пользователя')
    def test_change_login_user_unauthorized(self, default_user):
        access_token = None
        update_login = default_user['email'][1:]
        update_payload = {'email': update_login}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 401 and 'You should be authorised' in update_response.text

    @allure.title('Проверка изменения пароля авторизованного пользователя')
    def test_change_password_user_authorized(self, default_user):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        update_password = default_user['password'][1:]
        update_payload = {'password': update_password}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 200 and update_response.json()['user']['email'] == default_user['email']

    @allure.title('Проверка изменения пароля неавторизованного пользователя')
    def test_change_password_user_unauthorized(self, default_user):
        access_token = None
        update_password = default_user['password'][1:]
        update_payload = {'password': update_password}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 401 and 'You should be authorised' in update_response.text

    @allure.title('Проверка изменения имени авторизованного пользователя')
    def test_change_name_user_authorized(self, default_user, get_payload):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        update_name = get_payload['name'][1:]
        update_payload = {'name': update_name}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 200 and update_response.json()['user']['name'] == update_name

    @allure.title('Проверка изменения имени неавторизованного пользователя')
    def test_change_name_user_unauthorized(self, default_user, get_payload):
        access_token = None
        update_name = get_payload['name'][1:]
        update_payload = {'name': update_name}
        update_response = UserApi.change_user_info(update_payload, access_token)

        assert update_response.status_code == 401 and 'You should be authorised' in update_response.text

    @allure.title('Проверка изменения логина на логин, который уже используется')
    def test_change_login_to_exist_login(self, default_user, remove_user):
        login_response = UserApi.login_user(default_user)
        access_token_1 = login_response.json()['accessToken']
        payload_second_user = data.generate_payload_for_user()
        response_second_user = UserApi.create_user(payload_second_user)
        access_token_2 = response_second_user.json()['accessToken']
        update_login = payload_second_user['email']
        update_payload = {'email': update_login}
        update_response = UserApi.change_user_info(update_payload, access_token_1)
        remove_user(access_token_2)

        assert update_response.status_code == 403 and 'User with such email already exists' in update_response.text
