import pytest
from base.base_client import get, post, delete
from payloads.store_payload import new_order

ORDER_ID = 88801


class TestStore:
    def test_get_inventory(self):
        response = get("/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_create_order(self):
        payload = new_order(ORDER_ID, pet_id=1)
        response = post("/store/order", payload)
        assert response.status_code == 200
        assert response.json()["id"] == ORDER_ID

    def test_get_order_by_id(self):
        response = get(f"/store/order/{ORDER_ID}")
        assert response.status_code == 200
        assert response.json()["status"] == "placed"

    def test_delete_order(self):
        response = delete(f"/store/order/{ORDER_ID}")
        assert response.status_code == 200
