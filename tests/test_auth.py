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

    assert data["username"] == "fardeen123"
    assert data["email"] == "fardeen123@gmail.com"


def test_register_duplicate_username(client):
    payload = {
        "name": "Fardeen",
        "username": "duplicateuser",
        "email": "dup1@gmail.com",
        "password": "testpassword123"
    }

    # First registration should work
    first_response = client.post("/user/register", json=payload)
    assert first_response.status_code == 201

    # Second registration with same username should fail
    second_payload = {
        "name": "Another User",
        "username": "duplicateuser",
        "email": "dup2@gmail.com",
        "password": "anotherpassword123"
    }

    second_response = client.post("/user/register", json=second_payload)

    assert second_response.status_code == 400
    assert "username already exist" in second_response.json()["detail"]


def test_login_user(client):
    register_payload = {
        "name": "Fardeen",
        "username": "loginuser",
        "email": "loginuser@gmail.com",
        "password": "testpassword123"
    }

    # Register first
    client.post("/user/register", json=register_payload)

    login_payload = {
        "username": "loginuser",
        "password": "testpassword123"
    }

    response = client.post("/user/login", json=login_payload)

    assert response.status_code == 200
    data = response.json()

    assert "token" in data


def test_login_wrong_password(client):
    register_payload = {
        "name": "Wrong Password User",
        "username": "wrongpassuser",
        "email": "wrongpass@gmail.com",
        "password": "correctpassword123"
    }

    client.post("/user/register", json=register_payload)

    wrong_login_payload = {
        "username": "wrongpassuser",
        "password": "wrongpassword123"
    }

    response = client.post("/user/login", json=wrong_login_payload)

    assert response.status_code == 401
    assert "wrong password" in response.json()["detail"].lower()