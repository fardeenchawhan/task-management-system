from fastapi import APIRouter,Depends, status,Query
from src.task import controller
from src.task.ditos import TaskSchema,TaskUpdateSchema,TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import Usermodel 




task_routes= APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
    )
 
@task_routes.post(
        "",
        summary="Create a new task",
        description="Creates a new task for the authenticated user with title, description, priority, status, and optional due date.",
        response_model=TaskResponseSchema,
        status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.create_task(body,db,user)

@task_routes.get(
        "",
        summary="Get all tasks",
        description="Returns a paginated list of all tasks belonging to the authenticated user.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def get_all_tasks(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated),page:int=Query(1,ge=1),limit:int=Query(10,ge=1,le=100)):
    return controller.get_all_tasks(db,user,page,limit)

@task_routes.get(
        "/search_task",
        summary="Search tasks",
        description="Searches tasks by title or description for the authenticated user.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def search_tasks(
    query: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated)   
):
    return controller.search_tasks(user,query,db)


@task_routes.get(
        "/due-tomorrow",
        summary="Get tasks due tomorrow",
        description="Returns all tasks that are scheduled to be due on the next day.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def due_tomorrow(db: Session = Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.due_tomorrow(db,user)

@task_routes.get(
        "/overdue",
        summary="Get overdue tasks",
        description="Returns all overdue tasks for the authenticated user that have passed their due date and are not completed.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def task_overdue(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.task_overdue(db,user)


@task_routes.get(
        "/priority/{priority}",
        summary="Filter tasks by priority",
        description="Returns tasks that match the specified priority level such as low, medium, or high.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def get_tasks_by_priority(
    priority: str,
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated),
):
    return controller.get_priority(priority,db,user)

@task_routes.get(
        "/status/{status}",
        summary="Filter tasks by status",
        description="Returns tasks that match the specified status such as pending, in_progress, or completed.",
        response_model=List[TaskResponseSchema],
        status_code=status.HTTP_200_OK)
def get_tasks_by_status(
    status: str,
    db: Session = Depends(get_db),
    user:Usermodel=Depends(is_authenticated),
):
    return controller.get_status(status,db,user)


@task_routes.get(
        "/{task_id}",
        summary="Get task details",
        description="Returns detailed information for a specific task belonging to the authenticated user.",
        response_model=TaskResponseSchema,
        status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.get_one_task(task_id,db,user)


@task_routes.put(
        "/update/{task_id}",
        summary="Update a task",
        description="Updates the details of an existing task including title, description, priority, status, and due date.",
        response_model=TaskResponseSchema,
        status_code=status.HTTP_200_OK)
def update_task(body:TaskUpdateSchema,task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.update_task(body,db,task_id,user)

@task_routes.delete(
        "/delete/{task_id}",
        summary="Delete a task",
        description="Deletes a specific task belonging to the authenticated user.",
        status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.delete_task(task_id,db,user)





