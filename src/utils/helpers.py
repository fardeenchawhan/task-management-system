from src.user.ditos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException,status,Request,Depends
from pwdlib import PasswordHash
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta
from src.utils.db import get_db





def is_authenticated(request:Request,db:Session=Depends(get_db)):
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



    
    