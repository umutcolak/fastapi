from api.calculation_helper import CalculationHelper
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_result_for_factorial_operation():
    """Test check post request result for factorial operation"""

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
    result = CalculationHelper.factorial(params["params"])
    assert response_body["factorial_result = "] == result
