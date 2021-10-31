import requests
import json

host = "http://127.0.0.1:8000/"


class BaseHelper:

    @staticmethod
    def get_request_for_endpoint(operation, params, headers):
        endpoint = host + operation
        response = requests.get(endpoint, params=params, headers=headers)
        response_body_json = json.loads(response.text)
        return response, response_body_json

    @staticmethod
    def post_request_for_endpoint(operation, params, headers):
        endpoint = host + operation
        response = requests.post(endpoint, params=params, headers=headers)
        response_body_json = json.loads(response.text)
        return response, response_body_json
