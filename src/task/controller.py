from src.task.ditos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import Taskmodel

def create_task(body:TaskSchema, db:Session):
    data=body.model_dump()
    new_task=Taskmodel(title=data['title'],description=data['description'],is_completed=data['is_completed'])
    db.add(new_task)
    db.commit()
    db.refresh(new_task)


    return {"message":"task created successfully", "data":new_task}


def get_all_tasks(db:Session):
    tasks=db.query(Taskmodel).all()
    return {"message":"tasks retrieved successfully", "data":tasks}