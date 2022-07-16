import allure
from requests import sessions
from config import URL


def request(method, path, headers, **kwargs):
    if headers is None:
        headers = {
            # "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    url = URL + path
    with sessions.Session() as session:
        return session.request(method=method, url=url, headers=headers, **kwargs)


def get(path, data=None, headers=None, **kwargs):
    with allure.step(f"GET request to path '{path}'"):
        return request("get", path, params=data, headers=headers, **kwargs)


def post(path, data=None, json=None, headers=None, **kwargs):
    with allure.step(f"POST request to path '{path}'"):
        return request("post", path, data=data, json=json, headers=headers, **kwargs)
