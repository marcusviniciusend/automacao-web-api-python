import pytest
from base.base_client import get, post, put, delete
from payloads.user_payload import new_user

USERNAME = "testuser_p2"


class TestUser:
    def test_create_user(self):
        payload = new_user(77701, USERNAME, "test@email.com", "senha123")
        response = post("/user", payload)
        assert response.status_code == 200

    def test_get_user_by_username(self):
        response = get(f"/user/{USERNAME}")
        assert response.status_code == 200
        assert response.json()["username"] == USERNAME

    def test_update_user(self):
        payload = new_user(77701, USERNAME, "novo@email.com", "senha456")
        response = put(f"/user/{USERNAME}", payload)
        assert response.status_code == 200

    def test_create_users_with_array(self):
        users = [new_user(77702, "arrayuser1", "array1@email.com", "pass1")]
        response = post("/user/createWithArray", users)
        assert response.status_code == 200

    def test_create_users_with_list(self):
        users = [new_user(77703, "listuser1", "list1@email.com", "pass1")]
        response = post("/user/createWithList", users)
        assert response.status_code == 200

    def test_login(self):
        response = get(
            "/user/login", params={"username": USERNAME, "password": "senha123"})
        assert response.status_code == 200

    def test_logout(self):
        response = get("/user/logout")
        assert response.status_code == 200

    def test_delete_user(self):
        response = delete(f"/user/{USERNAME}")
        assert response.status_code == 200
