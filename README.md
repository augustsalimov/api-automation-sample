# About

This is python scripted sample of testing of API. <br>
Tasks: <br>
1) Get a list of users (GET https://reqres.in/api/users?page=2) and validate that all fields are received. <br>
2) Create user (POST https://reqres.in/api/users) using data and check the server response.

## Tools

`Python 3` using the `pytest`, `requests` and the `allure` for reports. 

## How to install?

Clone this git repository: 
```
with http: git clone https://github.com/augustsalimov/api-automation-sample.git
with ssh: git clone git@github.com:augustsalimov/api-automation-sample.git
```
Then install virtual environment and activate it: 
```
python3 -m venv venv
source venv/bin/activate
```
Optional. Update pip: `pip install -U pip`
Install all requirements: `pip install -r requirements.txt`

## How to run?

To run use command: `pytest tests` <br>

Options: <br>
`--collect-only` - list of all tests; <br> 
`-s` - to output all prints; <br>
`-lf` - restart test that failed last time. <br>

To generate allure report use commands:
```
pytest tests
allure serve allure-results
```
