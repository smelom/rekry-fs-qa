import requests
from requests.adapters import HTTPAdapter, Retry

API_URL = "https://dummy.restapiexample.com/api/v1"
EMPLOYEE_DATA = {
    "name": "Test Tester",
    "salary": "1234.56",
    "age": "50",
}

# Use retries to avoid the pain of "429 Too Many Requests"
session = requests.Session()
retries = Retry(total=4, backoff_factor=16, status_forcelist=[429, 405])
session.mount(API_URL, HTTPAdapter(max_retries=retries))
# The API returns 406 with the default UA python-requests/2.28.1, so need to set it to something else
session.headers.update({"User-Agent": "Mozilla 5.0"})


def test_get_employees_check_status_code_equals_200():
    response = session.get(f"{API_URL}/employees")
    assert response.status_code == 200


def test_get_employees_check_content_type_equals_json():
    response = session.get(f"{API_URL}/employees")
    assert response.headers["Content-Type"] == "application/json"


def test_get_employee_with_id_1_check_status_code_equals_200():
    response = session.get(f"{API_URL}/employee/1")
    assert response.status_code == 200


def test_create_employee_check_status_code_equals_200():
    response = session.post(f"{API_URL}/create", json=EMPLOYEE_DATA)
    assert response.status_code == 200


def test_create_employee_check_response_data():
    response = session.post(f"{API_URL}/create", json=EMPLOYEE_DATA)
    response_body = response.json()
    for key, value in EMPLOYEE_DATA.items():
        assert response_body["data"][key] == value
    assert "id" in response_body["data"]


def test_update_employee_check_status_code_equals_200():
    response = session.put(f"{API_URL}/update/1", json=EMPLOYEE_DATA)
    assert response.status_code == 200
