from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = 'USERS'
    __table_args__ = {'schema': 'MASTR'}

    SID = Column(Integer, primary_key=True, autoincrement=True)
    USERID = Column(String(50), nullable=True)
    ACTIVE = Column(String(1), nullable=True)  # Assuming ACTIVEFLAG is a single character
    EMAIL = Column(String(255), nullable=True)  # Adjust length as necessary
