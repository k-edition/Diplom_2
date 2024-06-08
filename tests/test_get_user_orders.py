from user_api import UserApi
from order_api import OrderApi
import data
import allure


class TestGetUserOrders:
    @allure.title('Проверка успешного получения заказов конкретного пользователя, который авторизован')
    def test_get_user_orders_authorized(self, default_user, create_order):
        login_response = UserApi.login_user(default_user)
        access_token = login_response.json()['accessToken']
        order_number = create_order(access_token)
        response = OrderApi.get_user_orders(access_token)

        assert response.status_code == 200 and response.json()['orders'][0]['number'] == order_number

    class TestGetUserOrders:
        @allure.title('Проверка ошибки при попытке получения заказов пользователя, который неавторизован')
        def test_get_user_orders_unauthorized(self, default_user, create_order):
            login_response = UserApi.login_user(default_user)
            access_token = login_response.json()['accessToken']
            create_order(access_token)
            response = OrderApi.get_user_orders(None)

            assert response.status_code == 401 and data.text[401][1] in response.text
