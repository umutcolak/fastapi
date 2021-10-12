from api.calculation_helper import CalculationHelper
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_multiplication_operation():
    """açıklama"""

    operation = "multiplication"
    params = {
        'params': "5,5,5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 200
    result = CalculationHelper.multiplication(params["params"])
    assert response_body["multiplication_result = "] == result
