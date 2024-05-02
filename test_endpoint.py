import requests


# Users endpoint
usersURL = 'http://127.0.0.1:8000/users/'

example_id = "00000000-0000-0000-0000-000000000000"
example_user = {
    "id": example_id,
    "email": "mister@testing.com",
    "full_name": "Testing Doe",
    "password": "weakpassword"
}

def test_list_users():
    r = requests.get(url=usersURL)
    assert r.status_code == 200

def test_create_user():
    r = requests.post(url=usersURL, json=example_user)
    assert r.status_code == 201

def test_find_user():
    r = requests.get(url=usersURL+example_id)
    assert r.status_code == 200

# def test_update_user():
#     example_user_mod = example_user.copy()
#     example_user_mod["full_name"] = "Testing Doe 2.0"
#     r = requests.put(url=usersURL+example_id, json=example_user_mod)
#     assert r.status_code == 200

def test_delete_user():
    r = requests.delete(url=usersURL+example_id)
    assert r.status_code == 200