from fastapi import APIRouter, HTTPException,Depends
from src.task import controller
from src.task.ditos import TaskSchema
from src.utils.db import get_db


task_routes= APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:TaskSchema,db=Depends(get_db)):
    return controller.create_task(body,db)