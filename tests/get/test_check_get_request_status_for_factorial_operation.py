from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_factorial_operation():
    """test check post request status for factorial operation"""

    operation = "factorial"
    params = {
        'params': "5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 200

