from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_subtraction_operation():
    """açıklama"""

    operation = "subtraction"
    params = {
        'params': ""
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 422
    error = ErrorConfig.not_correct_params
    assert response_body["detail"] == error
