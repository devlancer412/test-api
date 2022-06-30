from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi import BackgroundTasks

from dotenv import load_dotenv
load_dotenv('.env')

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')     # should be kept secret
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')      # should be kept secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
	return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
	return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
	if expires_delta is not None:
		expires_delta = datetime.utcnow() + expires_delta
	else:
		expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	
	to_encode = {"exp": expires_delta, "sub": str(subject)}
	encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
	return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
	if expires_delta is not None:
		expires_delta = datetime.utcnow() + expires_delta
	else:
		expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
	
	to_encode = {"exp": expires_delta, "sub": str(subject)}
	encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
	return encoded_jwt

# email verification
class Envs:
	MAIL_USERNAME = os.getenv('MAIL_USERNAME')
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
	MAIL_FROM = os.getenv('MAIL_FROM')
	MAIL_PORT = int(os.getenv('MAIL_PORT'))
	MAIL_SERVER = os.getenv('MAIL_SERVER')
	MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')
 
conf = ConnectionConfig(
  MAIL_USERNAME=Envs.MAIL_USERNAME,
  MAIL_PASSWORD=Envs.MAIL_PASSWORD,
  MAIL_FROM=Envs.MAIL_FROM,
  MAIL_PORT=Envs.MAIL_PORT,
  MAIL_SERVER=Envs.MAIL_SERVER,
  MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
  MAIL_TLS=True,
  MAIL_SSL=False,
  USE_CREDENTIALS=True,
  # TEMPLATE_FOLDER='./templates/email'
)

async def send_email_async(subject: str, email_to: str, body: dict):
	message = MessageSchema(
		subject=subject,
		recipients=[email_to],
		body=body,
		subtype='html',
	)
	
	fm = FastMail(conf)
	await fm.send_message(message, template_name='email.html')

def send_email_background(background_tasks: BackgroundTasks, title: str, email_to: str, body: dict):
	message = MessageSchema(
		title=title,
		recipients=[email_to],
		body=body,
		subtype='html',
	)
	fm = FastMail(conf)
	background_tasks.add_task(
		fm.send_message, message, template_name='email.html')