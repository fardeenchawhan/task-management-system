from fastapi import APIRouter,Depends,status
from src.utils.db import get_db
from src.user.ditos import UserSchema,ResponseSchema,LoginSchema,ProfilUpdateSchema,ChangePasswordSchema
from sqlalchemy.orm import Session
from src.user import controller
from src.user.models import Usermodel
from src.utils.helpers import is_authenticated


user_routes=APIRouter(
    prefix="/user",
    tags=["Users"]
    )

@user_routes.post(
    "/register",
    summary="Register a new user",
    description="Creates a new user account and stores the hashed password.",
    response_model=ResponseSchema,
    status_code=status.HTTP_201_CREATED
    )
async def register(body:UserSchema,db:Session=Depends(get_db)):
    return await controller.register(body,db)


@user_routes.post(
    "/login",
    summary="Authenticate user",
    description="Validates credentials and returns a JWT access token.",
    status_code=status.HTTP_200_OK
    )
def login(body:LoginSchema,db:Session=Depends(get_db)):
    return controller.login_user(body,db)


@user_routes.get(
        "/profile",
         summary="Get user profile",
         description="Returns the profile information of the currently authenticated user.",
         status_code=status.HTTP_200_OK,
         response_model=ResponseSchema
         )
def get_profil(db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.get_profil(db,user)


@user_routes.put(
        "/profile_update",
        summary="Update user profile",
        description="Updates the authenticated user's profile information such as name, username, or email.",
        status_code=status.HTTP_200_OK,
        response_model=ResponseSchema
        )
async def update_profil(body:ProfilUpdateSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
     return await controller.update_profil(body,db,user)

@user_routes.put(
        "/change-password",
        summary="Change password",
        description="Allows the authenticated user to change their password after verifying the current password.",
        status_code=status.HTTP_200_OK
        )
def change_password(body:ChangePasswordSchema,db:Session=Depends(get_db),user:Usermodel=Depends(is_authenticated)):
    return controller.ChangePassword(body,db,user)
