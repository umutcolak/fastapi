from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_division_operation():
    """test check post request status for division operation"""

    operation = "division"
    params = {
        'params': "10,5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 200
    assert response_body["division_result = "] == 2
