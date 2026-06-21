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


def test_get_single_task(auth_client):
    payload = {
        "title": "Single task test",
        "description": "Create task before fetching one task",
        "status": "pending",
        "priority": "low",
        "due_date": "2026-06-27"
    }

    create_response = auth_client.post("/tasks", json=payload)
    assert create_response.status_code == 201

    created_task = create_response.json()
    task_id = created_task["id"]

    response = auth_client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Single task test"


def test_delete_task(auth_client):
    payload = {
        "title": "Task to delete",
        "description": "This task will be deleted",
        "status": "pending",
        "priority": "medium",
        "due_date": "2026-06-28"
    }

    create_response = auth_client.post("/tasks", json=payload)
    assert create_response.status_code == 201

    created_task = create_response.json()
    task_id = created_task["id"]

    delete_response = auth_client.delete(f"/tasks/delete/{task_id}")

    assert delete_response.status_code == 204


def test_update_task(auth_client):
    payload = {
        "title": "Old Task Title",
        "description": "Old task description",
        "status": "pending",
        "priority": "low",
        "due_date": "2026-06-29"
    }

    create_response = auth_client.post("/tasks", json=payload)
    assert create_response.status_code == 201

    task_id = create_response.json()["id"]

    update_payload = {
        "title": "Updated Task Title",
        "priority": "high"
    }

    response = auth_client.put(f"/tasks/update/{task_id}", json=update_payload)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Updated Task Title"
    assert data["priority"] == "high"
    assert data["description"] == "Old task description"


def test_search_task(auth_client):
    payload = {
        "title": "Searchable Task",
        "description": "This task should be found in search",
        "status": "pending",
        "priority": "medium",
        "due_date": "2026-06-30"
    }

    auth_client.post("/tasks", json=payload)

    response = auth_client.get("/tasks/search-task?query=Searchable")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["title"] == "Searchable Task"


def test_search_task_not_found(auth_client):
    response = auth_client.get("/tasks/search-task?query=this_task_does_not_exist")

    assert response.status_code == 404
    assert response.json()["detail"] == "task not found"


def test_filter_tasks_by_status(auth_client):
    payload = {
        "title": "Completed Task",
        "description": "Task for status filter test",
        "status": "completed",
        "priority": "low",
        "due_date": "2026-07-01"
    }

    auth_client.post("/tasks", json=payload)

    response = auth_client.get("/tasks/status/completed")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["status"] == "completed"


def test_filter_tasks_by_priority(auth_client):
    payload = {
        "title": "High Priority Task",
        "description": "Task for priority filter test",
        "status": "pending",
        "priority": "high",
        "due_date": "2026-07-02"
    }

    auth_client.post("/tasks", json=payload)

    response = auth_client.get("/tasks/priority/high")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["priority"] == "high"


def test_get_non_existing_task(auth_client):
    response = auth_client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"