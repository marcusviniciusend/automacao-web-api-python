def new_pet(pet_id: int, name: str, status: str = "available") -> dict:
    return {
        "id": pet_id,
        "name": name,
        "status": status,
        "photoUrls": [],
    }
