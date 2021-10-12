from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper


def test_check_post_request_status_for_multiplication_operation():
    """açıklama"""

    operation = "multiplication"
    params = {
        'params': "5,5,5"
    }
    headers = {
        'username': "",
        'password': ""
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 400
    error = ErrorConfig.empty_username_password
    assert response_body["detail"] == error
