def new_order(order_id: int, pet_id: int, quantity: int = 1, status: str = "placed") -> dict:
    return {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "status": status,
        "complete": False,
    }
