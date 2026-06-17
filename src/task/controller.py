from src.task.ditos import TaskSchema ,TaskUpdateSchema
from sqlalchemy.orm import Session 
from sqlalchemy import or_
from src.task.models import Taskmodel
from fastapi import HTTPException
from src.user.models import Usermodel
from datetime import date, timedelta
from src.utils.mail import send_task_reminder

def create_task(body:TaskSchema, db:Session,user:Usermodel):
    data=body.model_dump()
    new_task=Taskmodel(title=data['title'],description=data['description'],status=data['status'],priority=data['priority'],due_date=data['due_date'],user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    
    return new_task


def get_all_tasks(db:Session,user:Usermodel,page:int,limit:int):
    
    skip = (page - 1) * limit

    tasks = (
        db.query(Taskmodel)
        .filter(Taskmodel.user_id==user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return tasks
    
def search_tasks(user:Usermodel,query:str,db:Session):
    tasks = (
        db.query(Taskmodel)
        .filter(Taskmodel.user_id==user.id)
        .filter(
            or_(
                Taskmodel.title.ilike(f"%{query}%"),
                Taskmodel.description.ilike(f"%{query}%")
            )
        )
        .all()
    )
    if not tasks:
        raise HTTPException(status_code=404, detail="task not found")
       
    return tasks


def get_status(status:int,db:Session,user:Usermodel):
   tasks=(
        db.query(Taskmodel)
        .filter(Taskmodel.user_id==user.id)
        .filter(Taskmodel.status == status)
        .all()
    )
   if not tasks:
        raise HTTPException(status_code=404, detail="task not found")
   
   return tasks


def get_priority(priority:int,db:Session,user:Usermodel):
   tasks=(
        db.query(Taskmodel)
        .filter(Taskmodel.user_id==user.id)
        .filter(Taskmodel.priority == priority)
        .all()
    )
   if not tasks:
        raise HTTPException(status_code=404, detail="task not found")
   
   return tasks


def get_one_task(task_id:int, db:Session,user:Usermodel):
    
    one_task=db.query(Taskmodel).get(task_id)
    if not one_task:
      raise HTTPException(status_code=404, detail="Task not found")
    
    if one_task.user_id != user.id:
      raise HTTPException(status_code=401, detail="You don't have access to this task")
    return one_task

def update_task(body:TaskUpdateSchema,db:Session,task_id:int,user:Usermodel):
    one_task=db.query(Taskmodel).get(task_id)
    old_due_date=one_task.due_date
    if not one_task:
      raise HTTPException(status_code=404, detail="Task not found")
    
    if one_task.user_id != user.id:
      raise HTTPException(status_code=401, detail="You cannot update this task")
    
    new_body=body.model_dump(exclude_unset=True)
    for field, value in new_body.items():
       setattr(one_task,field,value)

    if one_task.due_date != old_due_date:
       one_task.reminder_sent = False
    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task


def delete_task(task_id:int,db:Session,user:Usermodel):
    one_task=db.query(Taskmodel).get(task_id)
    if not one_task:
      raise HTTPException(status_code=404, detail="Task not found")
    if one_task.user_id != user.id:
      raise HTTPException(status_code=401, detail="You cannot delete this task")
       
       
    db.delete(one_task)
    db.commit()

    return None


def due_tomorrow(db:Session,user:Usermodel):
    tomorrow = date.today() + timedelta(days=1)

    tasks = (
        db.query(Taskmodel)
        .filter(Taskmodel.user_id==user.id)
        .filter(
            Taskmodel.due_date == tomorrow,
            Taskmodel.status != "completed"
        )
        .all()
    )
    if not tasks:
      raise HTTPException(status_code=404, detail="There is no task with the Due Date of Tomorrow")

    return tasks


def task_overdue(db:Session,user:Usermodel):
   day:date=date.today()
   tasks=(
      db.query(Taskmodel)
      .filter(
         Taskmodel.user_id==user.id,
         Taskmodel.due_date.is_not(None),
         Taskmodel.due_date<day,
         Taskmodel.status != "completed"
         )
      .all())
   
   if not tasks:
      raise HTTPException(status_code=404, detail="There is no overdue date task")
   return tasks
      

   






