# Task Management System API

## API Documentation Preview

![Swagger UI](images/Swagger-ui.png)

---

## Live Demo

* **API Base URL:** https://task-management-system-650m.onrender.com
* **Swagger UI:** https://task-management-system-650m.onrender.com/docs
* **ReDoc:** https://task-management-system-650m.onrender.com/redoc

---

## Overview

Task Management System API is a backend application built with FastAPI that allows users to create, manage, and track tasks efficiently.

The system includes secure JWT authentication, task filtering, pagination, email notifications, automated reminders, and user profile management.

This project demonstrates modern backend development practices using FastAPI, SQLAlchemy, PostgreSQL, Alembic, APScheduler, Docker, automated testing, and CI with GitHub Actions.

---

## Features

### Authentication & User Management

* User Registration
* User Login
* JWT Authentication
* Get User Profile
* Update User Profile
* Change Password

### Task Management

* Create Task
* Get All Tasks
* Get Single Task
* Update Task
* Delete Task

### Task Utilities

* Pagination
* Search Tasks by Title or Description
* Filter Tasks by Status
* Filter Tasks by Priority
* Due Tomorrow Tasks
* Overdue Tasks

### Notifications

* Registration Confirmation Email
* Due Date Reminder Email
* Automated Reminder Scheduling using APScheduler

### System

* Health Check Endpoint
* Interactive Swagger Documentation
* ReDoc Documentation
* Docker Support
* Cloud Deployment
* Automated Testing
* GitHub Actions CI

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* APScheduler
* FastAPI-Mail
* Pydantic
* Docker
* Pytest
* GitHub Actions
* Python

---

## Technical Highlights

* Built using FastAPI and SQLAlchemy
* JWT-based Authentication and Authorization
* PostgreSQL Database Integration
* Alembic Database Migrations
* Docker Containerization
* APScheduler Background Jobs
* Automated Email Notification System
* Pagination, Search, and Filtering Support
* Environment-based Configuration Management
* Interactive API Documentation using Swagger UI
* Automated testing with Pytest
* Continuous Integration using GitHub Actions
* Cloud Deployment using Render

---

## Project Structure

```text
task-management-system/
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── alembic/
│
├── images/
│   └── Swagger-ui.png
│
├── src/
│   ├── scheduler/
│   │   └── reminder_scheduler.py
│   │
│   ├── task/
│   │   ├── controller.py
│   │   ├── ditos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── controller.py
│   │   ├── ditos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── db.py
│       ├── helpers.py
│       ├── mail.py
│       └── settings.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_tasks.py
│
├── .env
├── .gitignore
├── alembic.ini
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/fardeenchawhan/task-management-system.git
cd task-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add the following:

```env
DB_CONNECTION=
SECRET_KEY=
ALGORITHM=
EXPIRY_TIME=

MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
```

---

## Database Migration

Run Alembic migrations:

```bash
alembic upgrade head
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

---

## API Documentation

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Docker

### Build Docker Image

```bash
docker build -t task-management-system .
```

### Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 task-management-system
```

### Access Application

```text
http://localhost:8000/docs
```

---

## Running Tests

The project includes automated tests for authentication and task management flows.

### Run tests locally

```bash
pytest
```

---

## Continuous Integration

GitHub Actions is configured to automatically run the test suite on every push and pull request.

This helps ensure that changes do not break existing functionality and keeps the project stable over time.

---

## User Endpoints

| Method | Endpoint                | Description                            |
| ------ | ----------------------- | -------------------------------------- |
| POST   | `/user/register`        | Register a new user                    |
| POST   | `/user/login`           | Authenticate user and return JWT token |
| GET    | `/user/profile`         | Get authenticated user's profile       |
| PUT    | `/user/profile_update`  | Update authenticated user's profile    |
| PUT    | `/user/change-password` | Change authenticated user's password   |

---

## Task Endpoints

| Method | Endpoint                     | Description                          |
| ------ | ---------------------------- | ------------------------------------ |
| POST   | `/tasks`                     | Create a new task                    |
| GET    | `/tasks`                     | Get paginated list of tasks          |
| GET    | `/tasks/search-task`         | Search tasks by title or description |
| GET    | `/tasks/due-tomorrow`        | Get tasks due tomorrow               |
| GET    | `/tasks/overdue`             | Get overdue tasks                    |
| GET    | `/tasks/priority/{priority}` | Filter tasks by priority             |
| GET    | `/tasks/status/{status}`     | Filter tasks by status               |
| GET    | `/tasks/{task_id}`           | Get a single task                    |
| PUT    | `/tasks/update/{task_id}`    | Update a task                        |
| DELETE | `/tasks/delete/{task_id}`    | Delete a task                        |

---

## Health Check

| Method | Endpoint  | Description             |
| ------ | --------- | ----------------------- |
| GET    | `/health` | Check if API is running |

---

## Authentication

The API uses **JWT Bearer Authentication**.

After login, include the access token in the `Authorization` header:

```http
Authorization: Bearer <your_access_token>
```

You can also authorize directly through Swagger UI using the **Authorize** button.

---

## Automated Email Reminders

The application uses APScheduler to automatically send reminder emails for tasks that are due the next day.

Reminder emails are sent only once per task using the `reminder_sent` flag.

---

## Deployment

The application is deployed on **Render** using **Docker** and **PostgreSQL**.

### Deployment Stack

* Render Web Service
* Render PostgreSQL Database
* Docker
* FastAPI
* SQLAlchemy

### Production Notes

Email notifications are implemented using FastAPI-Mail and Gmail SMTP.

Email functionality works correctly in local environments. Cloud deployment may require an email provider such as **Resend**, **SendGrid**, or **Mailgun** due to SMTP restrictions imposed by some hosting providers.

---

## Future Improvements

* Role-Based Access Control (RBAC)
* Integration Testing for more complete API coverage
* Redis Caching
* Production Email Service Integration (Resend/SendGrid)
* API Rate Limiting
* WebSocket Notifications
* Admin Dashboard / Analytics Layer

---

## What I Learned

Through this project I gained hands-on experience with:

* REST API Design
* Authentication and Authorization
* PostgreSQL Database Design
* ORM Development with SQLAlchemy
* Database Migrations using Alembic
* Docker Containerization
* Cloud Deployment using Render
* Background Task Scheduling
* Email Integration
* Environment Variable Management
* API Documentation
* Automated Testing
* Continuous Integration with GitHub Actions
* Software Project Structure

---

## Author

**Fardeen Chawhan**


