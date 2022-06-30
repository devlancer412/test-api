from turtle import title
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
  first_name: str = Field(None, title='First name', max_length=512)
  last_name: str = Field(None, title='First name', max_length=512)
  
class EmailUserBase(UserBase):
  email: EmailStr = Field(title = 'Email address')
  password: str = Field(title = 'Password')
  
class Signature(BaseModel):
  r: str = Field(title = "Signature r")
  s: str = Field(title = "Signature s")
  v: int = Field(title = "Signature v")
  
class WalletUserBase(UserBase):
  wallet: str = Field(title = 'Wallet address')
  password: str = Field(title = 'Password')
  signature: Signature
  
class AccessKey(BaseModel):
  id: int
  is_pending: bool
  key: str

class User(UserBase):
  id: int
  deleted: bool
  access_key: AccessKey
  
  class Config:
    orm_mode = True