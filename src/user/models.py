from sqlalchemy import Column,Integer,String,Boolean,String,DateTime
from src.utils.db import Base
from sqlalchemy.orm import relationship

class Usermodel(Base):
    __tablename__="user_table"

    id=Column(Integer,primary_key=True)
    name=Column(String)
    username=Column(String,nullable=False)
    email=Column(String)
    hash_password=Column(String,nullable=False)

    tasks = relationship(
        "Taskmodel",
        back_populates="user",
        cascade="all, delete"
    )

    

