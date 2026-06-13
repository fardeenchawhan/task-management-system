from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title:str
    description:str
    is_completed:bool=False

class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TaskResponseSchema(BaseModel):
    id:int
    title:str
    description:str
    is_completed:bool
    user_id:int | None =0