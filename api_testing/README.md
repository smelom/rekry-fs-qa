# API testing

## Test cases

### What to test

TODO: _Explain what you would test_

- HTTP status codes
- Response headers
- Response payload
- Error codes

- Positive and negative test cases
- Valid and invalid inputs

- Requests in isolation
- Workflows containing several requests
  - E.g. create employee, update employee data, get employee data, delete employee

### Top 5 test cases

TODO: _Choose your top 5-6 top test cases and explain why you prioritised those_


## Automating the tests

### Chosen tools

[Python](https://www.python.org/) was chosen as the tool for this assignment, with
[pytest](https://docs.pytest.org/en/7.2.x/) as the testing framework and
[requests](https://requests.readthedocs.io/en/latest/) as the HTTP library.

Python is very easily extensible. It gives us the flexibility to combine the API testing with other types of testing,
for example GUI testing if needed. Both `pytest` and `requests` are very commonly used and easy to get started with.

## Running the tests

TODO: _Automate one or more of those top test cases in your chosen language/using chosen tools_

### Requirements

Python version 3.9+

Required Python dependencies are listed in the `requirements.txt` file. These need to be installed before running the
program. This can be done by running the following command:

```
pip install -r requirements.txt
```

(Using a [virtual environment](https://docs.python.org/3/library/venv.html) is highly recommended!)

### Usage

```
pytest test_dummy_api.py
```
