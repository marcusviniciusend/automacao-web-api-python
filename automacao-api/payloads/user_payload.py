def new_user(user_id: int, username: str, email: str, password: str) -> dict:
    return {
        "id": user_id,
        "username": username,
        "email": email,
        "password": password,
        "userStatus": 1,
    }
