from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.models import Taskmodel
from src.task.router import task_routes
from src.user.router import user_routes
from src.scheduler.reminder_scheduler import scheduler


Base.metadata.create_all(engine)
app= FastAPI()
app.include_router(task_routes)
app.include_router(user_routes)

@app.on_event("startup")
async def startup_event():
    scheduler.start()

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }