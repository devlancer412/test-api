from schemas.user import AccessKey
from fastapi import APIRouter, status, HTTPException, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from operator import and_

from utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password,
    send_email_background
)
from schemas.user import EmailUserBase
from schemas.auth import TokenSchema
from models.user import User, UserAccessKey
from dependencies.database_deps import get_db_session
from dependencies.auth_deps import get_current_user_from_email_oauth, get_current_user_from_wallet_oauth

router = APIRouter(
  prefix='/auth',
  tags=['auth'],
  responses={404: {"description": "Not found"}},
)


@router.post('/signup/email', summary="Create new user",)
async def create_user_by_email(data: EmailUserBase, session: Session = Depends(get_db_session)):
  # querying database to check if user already exist
  user = session.query(User).filter(and_(User.email == data.email, User.deleted == False)).first()
  if user is not None:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="User with this email already exist"
    )
  
  new_user = User()
  new_user.first_name = data.first_name
  new_user.last_name = data.last_name
  new_user.email = data.email
  new_user.hashed_password = get_hashed_password(data.password)
  
  session.add(new_user)
  session.flush()
  session.refresh(new_user, attribute_names=['id'])
  data = {'user_id': new_user.id}
  new_access_key = UserAccessKey()
  new_access_key.is_pending = True
  new_access_key.key = "123456"
  new_access_key.user_id = new_user.id
  session.add(new_access_key)
  session.commit()
  return data

@router.post('/login/email', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db_session)):
  user: User = session.query(User, AccessKey).filter(and_(User.email == form_data.username, User.deleted == False)).first()
  if user is None:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Incorrect email or password"
    )

  if not verify_password(form_data.password, user.hashed_password):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Incorrect email or password"
    )
    
  if user.access_key.is_pending:
    # send_email_background(background_tasks, 'Hello your reaching out to Modern time', user.email, {'name': user.first_name + user.last_name, 'code': user.access_key.key})
    raise HTTPException(
      status_code=status.HTTP_403_FORBIDDEN,
      detail="You need to verify email"
    )
  
  return {
    "access_token": create_access_token(user.id),
    "refresh_token": create_refresh_token(user.id),
  }
  
@router.get('/me', summary='Get details of currently logged in user')
async def get_me(user: User = Depends(get_current_user_from_email_oauth)):
    return user
  