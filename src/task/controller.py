from src.task.ditos import TaskSchema ,TaskUpdateSchema
from sqlalchemy.orm import Session
from src.task.models import Taskmodel
from fastapi import HTTPException

def create_task(body:TaskSchema, db:Session):
    data=body.model_dump()
    new_task=Taskmodel(title=data['title'],description=data['description'],is_completed=data['is_completed'])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)


    return new_task


def get_all_tasks(db:Session):
    tasks=db.query(Taskmodel).all()
    return tasks

def get_one_task(task_id:int, db:Session):
    one_task=db.query(Taskmodel).get(task_id)
    if not one_task:
      raise HTTPException(status_code=404, detail="task not found")
    return one_task

def update_task(body:TaskUpdateSchema,db:Session,task_id:int):
    one_task=db.query(Taskmodel).get(task_id)
    if not one_task:
      raise HTTPException(status_code=404, detail="task not found")
    new_body=body.model_dump(exclude_unset=True)
    for field, value in new_body.items():
       setattr(one_task,field,value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task


def delete_task(task_id:int,db:Session):
    one_task=db.query(Taskmodel).get(task_id)
    if not one_task:
      raise HTTPException(status_code=404, detail="task not found")
    db.delete(one_task)
    db.commit()

    return None

   






