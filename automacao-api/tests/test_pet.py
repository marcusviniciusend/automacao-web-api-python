import pytest
from base.base_client import get, post, put, delete, post_form, post_file
from payloads.pet_payload import new_pet

PET_ID = 99901


class TestPet:
    def test_create_pet(self):
        payload = new_pet(PET_ID, "Rex")
        response = post("/pet", payload)
        assert response.status_code == 200
        assert response.json()["id"] == PET_ID

    def test_get_pet_by_id(self):
        response = get(f"/pet/{PET_ID}")
        assert response.status_code == 200
        assert response.json()["name"] == "Rex"

    def test_update_pet(self):
        payload = new_pet(PET_ID, "Rex Updated", status="sold")
        response = put("/pet", payload)
        assert response.status_code == 200
        assert response.json()["status"] == "sold"

    def test_update_pet_with_form(self):
        response = post_form(
            f"/pet/{PET_ID}", data={"name": "Rex Form", "status": "pending"})
        assert response.status_code == 200

    def test_upload_pet_image(self):
        response = post_file(f"/pet/{PET_ID}/uploadImage", b"fake-image-bytes")
        assert response.status_code == 200

    def test_find_pet_by_status(self):
        response = get("/pet/findByStatus", params={"status": "available"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self):
        response = delete(f"/pet/{PET_ID}")
        assert response.status_code == 200
