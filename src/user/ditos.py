
from pydantic import BaseModel,EmailStr

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
