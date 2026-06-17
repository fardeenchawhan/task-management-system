
from sqlalchemy.orm import Session
from src.user.models import Usermodel
from fastapi import HTTPException,Depends
import jwt
from src.utils.settings import settings
from jwt.exceptions import InvalidTokenError
from src.utils.db import get_db
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def is_authenticated(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    try:
        token = credentials.credentials

        data = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = data.get("id")

        user = (
            db.query(Usermodel)
            .filter(Usermodel.id == user_id)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="You are unauthorized"
            )

        return user

    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="You are unauthorized"
        )

    