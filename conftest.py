import pytest
import helper
from user_api import UserApi
from order_api import OrderApi


@pytest.fixture(scope='function')
def get_payload():
    payload = helper.GenerateData.generate_payload_for_user()

    return payload


@pytest.fixture(scope='function')
def default_user(get_payload, remove_user):
    create_response = UserApi.create_user(get_payload)
    login_payload = helper.ModifyData.modify_payload_for_login_user(get_payload)
    access_token = create_response.json()['accessToken']

    yield login_payload

    remove_user(access_token)


@pytest.fixture(scope='function')
def remove_user(request):
    def _remove_user(token):
        UserApi.delete_user(token)

    return _remove_user


@pytest.fixture(scope='function')
def create_order(request):
    def _create_order(token):
        payload = {'ingredients': helper.GenerateData.generate_payload_for_order()}
        order_response = OrderApi.create_order(payload, token)
        order_number = order_response.json()['order']['number']
        return order_number

    return _create_order
