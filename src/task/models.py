from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Date
from src.utils.db import Base

class Taskmodel(Base):
    __tablename__="user_tasks"

    id=Column(Integer, primary_key=True)
    title=Column(String)
    description=Column(String)
    status=Column(String, default="pending")
    priority=Column(String)
    due_date=Column(Date,nullable=True)

    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"))