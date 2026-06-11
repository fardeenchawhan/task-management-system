from fastapi import APIRouter, HTTPException,Depends, status
from src.task import controller
from src.task.ditos import TaskSchema,TaskUpdateSchema,TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session



task_routes= APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session=Depends(get_db)):
    return controller.create_task(body,db)

@task_routes.get("/all_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db)):
    return controller.get_all_tasks(db)

@task_routes.get("/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session=Depends(get_db)):
    return controller.get_one_task(task_id,db)

@task_routes.put("/update/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskUpdateSchema,task_id:int,db:Session=Depends(get_db)):
    return controller.update_task(body,db,task_id)

@task_routes.delete("/delete/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    return controller.delete_task(task_id,db)
