import data
import helper
from user_api import UserApi
from order_api import OrderApi
import allure


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа авторизованным пользователем')
    def test_create_order_authorized_user(self, default_user):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        payload = {'ingredients': data.generate_payload_for_order()}
        response = OrderApi.create_order(payload, access_token)

        assert response.status_code == 200 and response.json()['order']['number'] is not None

    @allure.title('Проверка ошибки при попытке создания заказа неавторизованным пользователем')
    def test_create_order_unauthorized_user(self):
        access_token = None
        payload = {'ingredients': data.generate_payload_for_order()}
        response = OrderApi.create_order(payload, access_token)

        assert response.status_code != 200  # в требованиях к API отсутствует код и текст ошибки для этого случая

    @allure.title('Проверка ошибки при попытке создания заказа без ингедиентов')
    def test_create_order_without_ingredients(self, default_user):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        payload = {'ingredients': []}
        response = OrderApi.create_order(payload, access_token)

        assert response.status_code == 400 and 'Ingredient ids must be provided' in response.text

    @allure.title('Проверка ошибки при попытке создания заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash(self, default_user):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        ingredients = data.generate_payload_for_order()
        invalid_ingredients = helper.ModifyData.modify_ingredients_for_order(ingredients)
        payload = {'ingredients': invalid_ingredients}
        response = OrderApi.create_order(payload, access_token)

        assert response.status_code == 500
