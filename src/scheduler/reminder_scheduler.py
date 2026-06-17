from datetime import date, timedelta
from sqlalchemy.orm import Session

from src.utils.db import LocalSession
from src.task.models import Taskmodel
from src.user.models import Usermodel
from src.utils.mail import send_task_reminder
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()


async def send_due_reminders():
    db: Session = LocalSession()

    try:
        tomorrow = date.today() + timedelta(days=1)

        tasks = (
           db.query(Taskmodel)
           .filter(
                  Taskmodel.due_date == tomorrow,
                  Taskmodel.status != "completed",
                  Taskmodel.reminder_sent == False
                )
           .all()
        )


        for task in tasks:

          await send_task_reminder(
            email=task.user.email,
            task_title=task.title,
            due_date=str(task.due_date)
          )

          task.reminder_sent = True
        db.commit()

    finally:
        db.close()


scheduler.add_job(
    send_due_reminders,
    trigger="interval",
    minutes=1
)