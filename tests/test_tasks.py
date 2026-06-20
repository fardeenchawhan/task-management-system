def test_create_task(auth_client):
    payload = {
        "title": "Finish pytest setup",
        "description": "Write task tests for the project",
        "status": "pending",
        "priority": "high",
        "due_date": "2026-06-25"
    }

    response = auth_client.post("/tasks", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Finish pytest setup"
    assert data["description"] == "Write task tests for the project"
    assert data["status"] == "pending"
    assert data["priority"] == "high"


def test_get_all_tasks(auth_client):
    # create one task first
    payload = {
        "title": "Get all tasks test",
        "description": "Task created before fetching all tasks",
        "status": "pending",
        "priority": "medium",
        "due_date": "2026-06-26"
    }

    auth_client.post("/tasks", json=payload)

    response = auth_client.get("/tasks?page=1&limit=10")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1