from src.user.ditos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException,status,Request
from pwdlib import PasswordHash
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta

password_hash=PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password,hash_password):
    return password_hash.verify(plain_password,hash_password)

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

def login_user(body:Usermodel,db:Session):
    user=db.query(Usermodel).filter(Usermodel.username==body.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have enter the wrong username")
    
    if not verify_password(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have enter the wrong password")
    
    exp_time=datetime.now()+timedelta(minutes=settings.EXPIRY_TIME)
    token=jwt.encode({"id":user.id,"exp":exp_time.timestamp()},settings.SECRET_KEY,settings.ALGORITHM)

    return {"token":token}


def is_authenticated(request:Request,db:Session):
    try:
        token=request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")
        
        token=token.split(" ")[-1]
        data=jwt.decode(token,settings.SECRET_KEY,settings.ALGORITHM)
        user_id=data.get("id")
        exp_time=int(data.get("exp"))


    

    
    
        is_user=db.query(Usermodel).filter(Usermodel.id==user_id).first()
        if not is_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")

        return is_user
    
    except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are unauthorized")



    
    