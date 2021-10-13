from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_get_request_empty_password_for_factorial_operation():
    """test check get request empty password for factorial operation"""

    operation = "factorial"
    params = {
        'params': "5"
    }
    headers = {
        'password': "",
        'username': Config.username
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 400
    error = ErrorConfig.empty_password
    assert response_body["detail"] == error
