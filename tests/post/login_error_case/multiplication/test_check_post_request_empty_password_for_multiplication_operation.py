from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_empty_password_for_multiplication_operation():
    """test check post request empty password for multiplication operation"""

    operation = "multiplication"
    params = {
        'params': "5,5,5"
    }
    headers = {
        'username': Config.username,
        'password': ""
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 400
    assert response_body["detail"] == ErrorConfig.empty_password
