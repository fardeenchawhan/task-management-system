from src.user.ditos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash=PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register(body:UserSchema,db:Session):
    is_user=db.query(Usermodel).filter(Usermodel.username==body.username).first()
    if is_user:
        raise HTTPException(400,detail="username already exist...")
    
    is_email=db.query(Usermodel).filter(Usermodel.email==body.email).first()
    if is_email:
        raise HTTPException(400,detail="email already exist...")
    
    hash_password=get_password_hash(body.password)

    new_user=Usermodel(
        name=body.name,
        username=body.username,
        email=body.email,
        hash_password=hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user