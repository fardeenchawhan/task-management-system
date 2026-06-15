from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskSchema(BaseModel):
    title:str
    description:str
    status:str
    priority:str
    due_date:date | None

class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date:Optional[date]=None

class TaskResponseSchema(BaseModel):
    id:int
    title:str
    description:str
    user_id:int | None =0
    status:str | None 
    priority:str | None
    due_date:date | None