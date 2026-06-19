from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.router import task_routes
from src.user.router import user_routes
from src.scheduler.reminder_scheduler import scheduler
from contextlib import asynccontextmanager


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()

    yield

    scheduler.shutdown()


app= FastAPI(
    title="Task Management System API",
    description="""
    A FastAPI-based task management system with:

    - JWT Authentication
    - Task CRUD Operations
    - Search & Filtering
    - Email Reminders
    - APScheduler Integration
    - User Profile Management
    """,
    version="1.0.0",
    lifespan=lifespan
)
app.include_router(task_routes)
app.include_router(user_routes)


@app.get(
    "/",
    tags=["System"],
    summary="API Information",
    description="Returns basic information about the Task Management System API."
)
def root():
    return {
        "message": "Task Management System API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health"
    }

@app.get(
        "/health",
        tags=["System"],
        summary="Health check",
        description="Checks whether the API service is running and available.",
        status_code=200
        )
def health():
    return {
        "status": "healthy"
    }