from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_subtraction_operation():
    """test check post request status for subtraction operation"""

    operation = "subtraction"
    params = {
        'params': "5,5,5,5,5,5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 422
    assert response_body["detail"] == ErrorConfig.post_more_params
