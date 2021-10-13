from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper


def test_check_get_request_empty_username_password_for_sum_operation():
    """test check get request empty username password for sum operation"""

    operation = "sum"
    params = {
        'params': "5"
    }
    headers = {
        'password': "",
        'username': ""
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 400
    error = ErrorConfig.empty_username_password
    assert response_body["detail"] == error
