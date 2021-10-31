import math


class CalculationHelper:
    @staticmethod
    def add(value, result=0):
        for i in map(int, value.split(",")):
            result += i
        return result

    @staticmethod
    def subtraction(value):
        array = (list(map(int, value.split(","))))
        first_result = list(map(int, value.split(",")))[0]
        for i in range(1, len(list(map(int, value.split(","))))):
            first_result = first_result - array[1]
            array.pop(0)
        return first_result

    @staticmethod
    def multiplication(value, result=1):
        for i in map(int, value.split(",")):
            result *= i
        return result

    @staticmethod
    def division(value):
        array = (list(map(int, value.split(","))))
        result = array[0]
        for array_index in array[1:]:
            result = result / array_index
        return int(result)

    @staticmethod
    def sum(value):
        return int((int(value) * (int(value) + 1)) / 2)

    @staticmethod
    def factorial(value):
        return math.factorial(int(value))
