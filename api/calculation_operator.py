from fastapi import HTTPException
from config import Config
from calculation_enum import PostCalculation, GetCalculation
from calculation_helper import CalculationHelper
from error_config import ErrorConfig


class CalculationOperator(CalculationHelper):
    @staticmethod
    def post_calculation_operator(operation, params, username):
        if operation == PostCalculation.ADD.value:
            return {"add_result = ": CalculationHelper.add(params), "username = ": username}
        elif operation == PostCalculation.SUBTRACTION.value:
            return {"subtraction_result = ": CalculationHelper.subtraction(params), "username = ": username}
        elif operation == PostCalculation.MULTIPLICATION.value:
            return {"multiplication_result = ": CalculationHelper.multiplication(params), "username = ": username}
        elif operation == PostCalculation.DIVISION.value:
            return {"division_result = ": CalculationHelper.division(params), "username = ": username}

    @staticmethod
    def get_calculation_operator(operation, params, username):
        if operation == GetCalculation.SUM.value:
            return {"sum_result = ": CalculationHelper.sum(params), "username = ": username}
        elif operation == GetCalculation.FACTORIAL.value:
            return {"factorial_result = ": CalculationHelper.factorial(params), "username = ": username}

    @staticmethod
    def check_post_parameter_count(operation, params, username, password):
        if params != "":
            if len((list(map(int, params.split(","))))) <= 5:
                return CalculationOperator.check_user_info(operation, params, username, password)
            else:
                raise HTTPException(status_code=422,
                                    detail=ErrorConfig.post_more_params)
        else:
            raise HTTPException(status_code=422,
                                detail=ErrorConfig.not_correct_params)

    @staticmethod
    def check_get_parameter_count(operation, params, username, password):
        if params != "":
            if len((list(map(int, params.split(","))))) == 1:
                return CalculationOperator.check_user_info(operation, params, username, password)
            else:
                raise HTTPException(status_code=422,
                                    detail=ErrorConfig.get_more_params)
        else:
            raise HTTPException(status_code=422,
                                detail=ErrorConfig.not_correct_params)

    @staticmethod
    def check_user_info(operation, params, username, password):
        if username == Config.username and password == Config.password:
            if operation in list(map(lambda calc: calc.value, PostCalculation._member_map_.values())):
                return CalculationOperator.post_calculation_operator(operation, params, username)
            elif operation in list(map(lambda calc: calc.value, GetCalculation._member_map_.values())):
                return CalculationOperator.get_calculation_operator(operation, params, username)
        elif username != Config.username and password == Config.password:
            raise HTTPException(status_code=400,
                                detail=ErrorConfig.empty_username)
        elif username == Config.username and password != Config.password:
            raise HTTPException(status_code=400,
                                detail=ErrorConfig.empty_password)
        elif username != Config.username and password != Config.password:
            raise HTTPException(status_code=400,
                                detail=ErrorConfig.empty_username_password)
