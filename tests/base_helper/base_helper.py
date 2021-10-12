from urllib import parse
import requests
import json

host = "http://127.0.0.1:8000/"


class BaseHelper:

    @staticmethod
    def get_request_for_endpoint(operation, params, headers):
        endpoint = host + operation
        response = requests.get(endpoint, params=params, headers=headers)
        response_body = json.loads(response.text)
        return response, response_body

    @staticmethod
    def post_request_for_endpoint(operation, params, headers):
        endpoint = host + operation
        params = parse.urlencode(params, safe=',')
        response = requests.post(endpoint, params=params, headers=headers)
        response_body = json.loads(response.text)
        return response, response_body
