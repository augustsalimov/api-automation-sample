import json
from requests import Response
from pathlib import Path


def json_check(response):
    try:
        return response.json()
    except json.JSONDecodeError:
        assert False, f"Response text '{response.text}' is not in JSON format"


def status_code(response: Response, expected_status_code):
    assert response.status_code == expected_status_code, \
        f"Unexpected status code! Expected {expected_status_code}, actual: {response.status_code}"


def json_has_keys(response: Response, keys: list):
    try:
        response_json = json_check(response)
        for key in keys:
            assert key in response_json, f"Response JSON doesn't have a key {key}"
    except AttributeError:
        for key in keys:
            assert key in response, f"Given dict doesn't have a key {key}"


def is_equal(left, right):
    assert left == right, f"'{left}' is not equal to '{right}'"


def return_fail(text):
    assert False, text

