from src.user.ditos import UserSchema,ProfilUpdateSchema
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException,status
from pwdlib import PasswordHash
import jwt
from src.utils.settings import settings
from datetime import datetime,timedelta
from src.utils.mail import send_email

password_hash=PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password,hash_password):
    return password_hash.verify(plain_password,hash_password)

async def register(body:UserSchema,db:Session):
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

    await send_email(
      emails=[new_user.email],
      subject="Registration Confirmation",
      body="""
        <h2>Welcome</h2>
        <p>Thanks for registering.</p>
        """
    )
    
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


def get_profil(db:Session,user:Usermodel):
    return user


async def update_profil(body:ProfilUpdateSchema,db:Session,user:Usermodel):
    old_email=user.email
    if body.email:
        existing_email=(
            db.query(Usermodel)
            .filter(
                Usermodel.email==body.email,
                Usermodel.id != user.id
            ).first()
        )
        
        if existing_email:
            raise HTTPException(
                    status_code=400,
                    detail="Email already exists"
            )
            
    if body.username:
        existing_username=(
            db.query(Usermodel)
            .filter(
                Usermodel.username==body.username,
                Usermodel.id != user.id   
            ).first()
        )

        if existing_username:
            raise HTTPException(
                    status_code=400,
                    detail="username already exists"
            )
    up_profil=body.model_dump(exclude_unset=True)
    for key ,value in up_profil.items():
        setattr(user,key,value)

    db.add(user)
    db.commit()
    db.refresh(user)
    if user.email!=old_email:
        try:
           await send_email(
              emails=[user.email],
              subject="Email Address Updated",
              body=f"""
                Your account email address has been updated successfully.

                  Old Email: {old_email}
                  New Email: {user.email}

                If you did not perform this action, please contact support immediately.

                """
            )
        except Exception as e:
           print("EMAIL ERROR:", str(e))

    return user


def ChangePassword(body,db,user):
    if not verify_password(body.old_password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You have enter the wrong password")
    
    if verify_password(body.new_password,user.hash_password):
        raise HTTPException(status_code=400,detail="New password must be different")
    
    new_password=get_password_hash(body.new_password)
    user.hash_password=new_password

    db.commit()


    return {
        "message": "Password updated successfully"
    }




    
    