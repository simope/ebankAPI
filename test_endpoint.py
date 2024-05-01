import requests


# Users endpoint
URL = 'http://127.0.0.1:8000/users/'

example_user = {
  "email": "mister@testing.com",
  "full_name": "Testing Doe",
  "password": "weakpassword"
}

def test_list_users():
    r = requests.get(url=URL)
    assert r.status_code == 200


def test_create_user():
    r = requests.post(url=URL, json=example_user)
    assert r.status_code == 201