from api.calculation_helper import CalculationHelper
from api.config import Config
from tests.base_helper.base_helper import BaseHelper


def test_check_post_request_status_for_sum_operation():
    """açıklama"""

    operation = "sum"
    params = {
        'params': "5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.get_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 200
    result = CalculationHelper.sum(params["params"])
    assert response_body["sum_result = "] == result
