from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = 'USERS'
    __table_args__ = {'schema': 'MASTR'}
    
    SID = Column(Integer, primary_key=True, autoincrement=True)
    USERID = Column(String)
    ACTIVE = Column(Boolean)
    EMAIL = Column(String)
    PASSWD = Column(String)
    SALT = Column(String)
    SUBMITDATE = Column(DateTime)
    FINALAPPROVEDATE = Column(DateTime)
    NAME_TH = Column(String)
    NAME_EN = Column(String)
    EMPLOYEEID = Column(String)
    TEL = Column(String)
    FAX = Column(String)
    STATUS_SID = Column(Integer)
    RECCREATE = Column(DateTime)
    RECUPDATE = Column(DateTime)
    RECBY = Column(String)
    MOBILE = Column(String)
