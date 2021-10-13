from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_sum_operation():
    """test check get request not correct params for sum operation"""

    operation = "sum"
    params = {
        'params': ""
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 422
    assert response_body["detail"] == ErrorConfig.not_correct_params
