from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
  __tablename__ = "user"
  id = Column(Integer, primary_key=True)
  first_name = Column(String(512), nullable=False)
  last_name = Column(String(512), nullable=False)
  email = Column(String(512), nullable=True)
  wallet = Column(String(64), nullable=True)
  hashed_password = Column(String(512), nullable=False)
  deleted = Column(Boolean, default=False)
  created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
  updated_at = Column(TIMESTAMP, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
  
  access_key = relationship('UserAccessKey', back_populates='user')
  
class UserAccessKey(Base):
  __tablename__ = "user_access_key"
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  is_pending = Column(Boolean, nullable=False, default=True)
  key = Column(String(6), nullable=False)
  
  user = relationship('User', back_populates='access_key')