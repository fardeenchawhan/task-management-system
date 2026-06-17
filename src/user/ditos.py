
from pydantic import BaseModel,EmailStr
from typing import Optional

class UserSchema(BaseModel):
    name:str
    username:str
    email:EmailStr
    password:str

class ResponseSchema(BaseModel):
    name:str
    username:str
    email:EmailStr
    id:int


class LoginSchema(BaseModel):
    username:str
    password:str

class ProfilUpdateSchema(BaseModel):
    name:Optional[str]=None
    username:Optional[str] = None
    email:Optional[EmailStr]=None


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str
