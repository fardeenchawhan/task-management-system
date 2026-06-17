from fastapi import APIRouter,Depends,status,Request
from src.utils.db import get_db
from src.user.ditos import UserSchema,ResponseSchema,LoginSchema,ProfilUpdateSchema,ChangePasswordSchema
from sqlalchemy.orm import Session
from src.user import controller
from src.user.models import Usermodel
from src.utils.helpers import is_authenticated


user_routes=APIRouter(prefix="/user")

@user_routes.post("/register",response_model=ResponseSchema,status_code=status.HTTP_201_CREATED)
async def register(body:UserSchema,db:Session=Depends(get_db)):
    return await controller.register(body,db)


@user_routes.post("/login",status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login_user(body,db)

@user_routes.get("/is_auth",status_code=status.HTTP_200_OK,response_model=ResponseSchema)
def is_auth(request:Request,db:Session=Depends(get_db)):
    return controller.is_authenticated(request,db)

@user_routes.get("/profil",status_code=status.HTTP_200_OK,response_model=ResponseSchema)
def get_profil(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.get_profil(db,user)


@user_routes.put("/profil_update",status_code=status.HTTP_201_CREATED,response_model=ResponseSchema)
def update_profil(body:ProfilUpdateSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.update_profil(body,db,user)

@user_routes.put("/change-password",status_code=status.HTTP_201_CREATED)
def change_password(body:ChangePasswordSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.ChangePassword(body,db,user)
