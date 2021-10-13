from api.calculation_helper import CalculationHelper
from tests.base_helper.base_helper import BaseHelper
from api.config import Config


def test_check_post_request_status_for_add_operation():
    """test check post request status for add operation"""

    operation = "add"
    params = {
        'params': "5,5,5"
    }
    headers = {
        'username': Config.username,
        'password': Config.password
    }
    response, response_body = BaseHelper.post_request_for_endpoint(operation=operation, params=params, headers=headers)
    assert response.status_code == 200
    result = CalculationHelper.add(params["params"])
    assert response_body["add_result = "] == result
