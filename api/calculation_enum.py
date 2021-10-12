from enum import Enum


class PostCalculation(Enum):
    ADD = "add"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"


class GetCalculation(Enum):
    SUM = "sum"
    FACTORIAL = "factorial"
