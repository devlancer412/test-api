from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from operator import and_
from datetime import datetime
from jose import jwt
from pydantic import ValidationError
from dependencies.database_deps import get_db_session
from models.user import User

from utils import (
  ALGORITHM,
  JWT_SECRET_KEY
)
from schemas.auth import TokenPayload

email_oauth = OAuth2PasswordBearer(
  tokenUrl="auth/login/email",
  scheme_name="JWT"
)

wallet_oauth = OAuth2PasswordBearer(
  tokenUrl="auth/login/wallet",
  scheme_name="JWT"
)

async def get_current_user_from_email_oauth(token: str = Depends(email_oauth), session: Session = Depends(get_db_session)) -> User:
  try:
    payload = jwt.decode(
      token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
    )
    token_data = TokenPayload(**payload)
    
    if datetime.fromtimestamp(token_data.exp) < datetime.now():
      raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
        headers={"WWW-Authenticate": "Bearer"},
      )
  except(jwt.JWTError, ValidationError):
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )
  
  user: User = session.query(User).filter(and_(token_data.sub == User.id, User.deleted == False)).first()
  
  if user is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Could not find user",
    )
  
  return user

async def get_current_user_from_wallet_oauth(token: str = Depends(wallet_oauth), session: Session = Depends(get_db_session)) -> User:
  try:
    payload = jwt.decode(
      token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
    )
    token_data = TokenPayload(**payload)
    
    if datetime.fromtimestamp(token_data.exp) < datetime.now():
      raise HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
        headers={"WWW-Authenticate": "Bearer"},
      )
  except(jwt.JWTError, ValidationError):
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},
    )
  
  user: User = session.query(User).filter(and_(token_data.sub == User.id, User.deleted == False)).first()
  
  if user is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Could not find user",
    )
  
  return user