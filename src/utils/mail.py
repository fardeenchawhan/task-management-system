from fastapi_mail import FastMail,MessageSchema,ConnectionConfig,MessageType
from pydantic import EmailStr,BaseModel
from typing import List
from src.utils.settings import settings





conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="from backend",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)




async def send_email(
    emails: List[str],
    subject: str,
    body: str
):
    message = MessageSchema(
        subject=subject,
        recipients=emails,
        body=body,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)

    return {"message": "mail has been sent"}



async def send_task_reminder(
    email: str,
    task_title: str,
    due_date: str
):
    body = f"""
    <h2>Task Reminder</h2>

    <p>Your task
    <strong>{task_title}</strong>
    is due on
    <strong>{due_date}</strong>.</p>

    <p>Please complete it before the deadline.</p>
    """

    await send_email(
        emails=[email],
        subject="Task Due Reminder",
        body=body
    )

# async def send_email(emails: List[str]):
#     html = """<p>Hi thanks for registeration our team will connect with you soon</p> """

#     message = MessageSchema(
#         subject="Registeration Confirmation",
#         recipients=emails,
#         body=html,
#         subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return {"message":"mail has been sent"}


