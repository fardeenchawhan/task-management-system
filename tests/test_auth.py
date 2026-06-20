def test_register_user(client):
    payload = {
        "name": "Fardeen",
        "username": "fardeen123",
        "email": "fardeen123@gmail.com",
        "password": "testpassword123"
    }

    response = client.post("/user/register", json=payload)

    assert response.status_code == 201
    data = response.json()

    # adjust this if your response schema is different
    assert data["username"] == "fardeen123"
    assert data["email"] == "fardeen123@gmail.com"


def test_login_user(client):
    register_payload = {
        "name": "Fardeen",
        "username": "loginuser",
        "email": "loginuser@gmail.com",
        "password": "testpassword123"
    }

    # register first
    client.post("/user/register", json=register_payload)

    login_payload = {
        "username": "loginuser",
        "password": "testpassword123"
    }

    response = client.post("/user/login", json=login_payload)

    assert response.status_code == 200
    data = response.json()

    assert "token" in data