# Task Management System API

## API Documentation Preview

![Swagger UI](images/Swagger-ui.png)

---

## Live Demo

### Deployed API

https://task-management-system-650m.onrender.com

### Swagger Documentation

https://task-management-system-650m.onrender.com/docs

### ReDoc Documentation

https://task-management-system-650m.onrender.com/redoc

---

## Overview

Task Management System API is a backend application built with FastAPI that allows users to create, manage, and track tasks efficiently.

The system includes secure JWT authentication, task filtering, pagination, email notifications, automated reminders, and user profile management.

This project demonstrates modern backend development practices using FastAPI, SQLAlchemy, PostgreSQL, Alembic, APScheduler, Docker, and FastAPI-Mail.

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
* Cloud Deployment using Render

---

## Project Structure

```text
task-management-system/
│
├── alembic/
├── src/
│   ├── task/
│   │   ├── controller.py
│   │   ├── models.py
│   │   ├── ditos.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── controller.py
│   │   ├── models.py
│   │   ├── ditos.py
│   │   └── router.py
│   │
│   ├── scheduler/
│   │   └── reminder_scheduler.py
│   │
│   └── utils/
│       ├── db.py
│       ├── helpers.py
│       ├── settings.py
│       └── mail.py
│
├── images/
│   └── Swagger-ui.png
│
├── main.py
├── requirements.txt
├── README.md
├── alembic.ini
├── Dockerfile
└── .gitignore
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

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

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

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Docker

## Build Docker Image

```bash
docker build -t task-management-system .
```

## Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 task-management-system
```

## Access Application

```text
http://localhost:8000/docs
```

---

## User Endpoints

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | /user/register        |
| POST   | /user/login           |
| GET    | /user/profile         |
| PUT    | /user/profile_update  |
| PUT    | /user/change-password |

---

## Task Endpoints

| Method | Endpoint                   |
| ------ | -------------------------- |
| POST   | /tasks                     |
| GET    | /tasks                     |
| GET    | /tasks/search-task         |
| GET    | /tasks/due-tomorrow        |
| GET    | /tasks/overdue             |
| GET    | /tasks/priority/{priority} |
| GET    | /tasks/status/{status}     |
| GET    | /tasks/{task_id}           |
| PUT    | /tasks/update/{task_id}    |
| DELETE | /tasks/delete/{task_id}    |

---

## Health Check

| Method | Endpoint |
| ------ | -------- |
| GET    | /health  |

---

## Authentication

The API uses JWT Bearer Authentication.

After login, include the access token in the Authorization header:

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

The application is deployed on Render using Docker and PostgreSQL.

### Deployment Stack

* Render Web Service
* Render PostgreSQL Database
* Docker
* FastAPI
* SQLAlchemy

### Production Notes

Email notifications are implemented using FastAPI-Mail and Gmail SMTP.

Email functionality works correctly in local environments. Cloud deployment may require an email provider such as Resend, SendGrid, or Mailgun due to SMTP restrictions imposed by some hosting providers.

---

## Future Improvements

* Role-Based Access Control (RBAC)
* Automated Unit Testing
* Integration Testing
* GitHub Actions CI/CD Pipeline
* Redis Caching
* Production Email Service Integration (Resend/SendGrid)
* API Rate Limiting
* WebSocket Notifications

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
* Software Project Structure

---

## Author

**Fardeen Chawhan**

