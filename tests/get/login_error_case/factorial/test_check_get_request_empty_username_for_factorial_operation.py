from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_get_request_empty_username_for_factorial_operation():
    """test check get request empty username for factorial operation"""

    operation = "factorial"
    params = {
        'params': "5"
    }
    headers = {
        'password': Config.password,
        'username': ""
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 400
    assert response_body["detail"] == ErrorConfig.empty_username
