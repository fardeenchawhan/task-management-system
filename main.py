from fastapi import FastAPI
from src.utils.db import Base,engine
from src.task.models import Taskmodel

Base.metadata.create_all(engine)
app= FastAPI()