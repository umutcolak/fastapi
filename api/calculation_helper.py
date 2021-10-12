import math


class CalculationHelper:
    @staticmethod
    def add(value, result=0):
        array = (list(map(int, value.split(","))))
        for array_index in range(len(array)):
            result = result + array[0]
            array.pop(0)
        return result

    @staticmethod
    def subtraction(value, result=0):
        array = (list(map(int, value.split(","))))
        for array_index in range(len(array)):
            result = result - array[0]
            array.pop(0)
        return result

    @staticmethod
    def multiplication(value, result=1):
        array = (list(map(int, value.split(","))))
        for array_index in range(len(array)):
            result = result * array[0]
            array.pop(0)
        return result

    @staticmethod
    def division(value, result=1):
        array = (list(map(int, value.split(","))))
        for array_index in range(len(array)):
            result = result / array[0]
            array.pop(0)
        return int(result)

    @staticmethod
    def sum(value):
        return (int(value) * (int(value) + 1)) / 2

    @staticmethod
    def factorial(value):
        return math.factorial(int(value))
