from fastapi import APIRouter, HTTPException,Depends, status,Query
from src.task import controller
from src.task.ditos import TaskSchema,TaskUpdateSchema,TaskResponseSchema
from src.utils.db import get_db
from typing import List,Dict
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import Usermodel
from src.task.models import Taskmodel
from datetime import date, timedelta
from src.scheduler.reminder_scheduler import send_due_reminders




task_routes= APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.create_task(body,db,user)

@task_routes.get("/all_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated),page:int=Query(1,ge=1),limit:int=Query(10,ge=1,le=100)):
    return controller.get_all_tasks(db,user,page,limit)

@task_routes.get("/search_task",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def search_tasks(
    query: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated)   
):
    return controller.search_tasks(user,query,db)


@task_routes.get("/due-tomorrow",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def due_tomorrow(db: Session = Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.due_tomorrow(db,user)

@task_routes.get("/overdue",response_model=List[TaskResponseSchema])
def task_overdue(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.task_overdue(db,user)


@task_routes.get("/priority/{priority}",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_tasks_by_priority(
    priority: str,
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated),
):
    return controller.get_priority(priority,db,user)

@task_routes.get("/status/{status}",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_tasks_by_status(
    status: str,
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated),
):
    return controller.get_status(status,db,user)


@task_routes.get("/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.get_one_task(task_id,db,user)


@task_routes.put("/update/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskUpdateSchema,task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.update_task(body,db,task_id,user)

@task_routes.delete("/delete/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.delete_task(task_id,db,user)





