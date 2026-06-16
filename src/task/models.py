from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Date
from src.utils.db import Base
from sqlalchemy.orm import relationship

class Taskmodel(Base):
    __tablename__="user_tasks"

    id=Column(Integer, primary_key=True)
    title=Column(String)
    description=Column(String)
    status=Column(String, default="pending")
    priority=Column(String)
    due_date=Column(Date,nullable=True)

    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"))

    reminder_sent = Column(
    Boolean,
    default=False,
    nullable=False
    )


    user = relationship(
        "Usermodel",
        back_populates="tasks"
    )