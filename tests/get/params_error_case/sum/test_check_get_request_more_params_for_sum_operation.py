from api.error_config import ErrorConfig
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_get_request_more_params_for_sum_operation():
    """test check get request more params for sum operation"""

    operation = "sum"
    params = {
        'params': "5,5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 422
    assert response_body["detail"] == ErrorConfig.get_more_params
