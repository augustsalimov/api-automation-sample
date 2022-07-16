import pytest
import allure
from email_validator import validate_email, EmailNotValidError
from lib import MyAssert, MyRequests
# from src.stdout import output_response


@allure.epic("All tests")
class TestAllTests:
    USER = {('kojima', 'genius'), ('алекс', 'программист'), ('12563', '9786')}


    @allure.title("Get user data")
    def test_get_user_data(self):
        response = MyRequests.get("/api/users?page=2")
        MyAssert.status_code(response, 200)
        MyAssert.json_has_keys(response, ['page', 'per_page', 'total', 'total_pages', 'data', 'support'])
        for dict_ in response.json()['data']:
            MyAssert.json_has_keys(dict_, ['id', 'email', 'first_name', 'last_name', 'avatar'])
            email = dict_['email']
            try:
                MyAssert.is_equal(email, validate_email(email).email)
            except EmailNotValidError as error:
                MyAssert.return_fail(str(error))

    @allure.title("Create user")
    @pytest.mark.parametrize('name, job', USER)
    def test_create_user(self, name, job):
        data = {'name': name, 'job': job}
        response = MyRequests.post("/api/users", json=data)
        MyAssert.status_code(response, 201)
        MyAssert.json_has_keys(response, ['name', 'job', 'id', 'createdAt'])
        MyAssert.is_equal(response.json()['name'], name)
        MyAssert.is_equal(response.json()['job'], job)
