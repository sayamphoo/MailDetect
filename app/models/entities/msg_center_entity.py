from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import NVARCHAR, BIT, DATETIME

Base = declarative_base()

class MsgCenterEntity(Base):
    __tablename__ = 'MSGCENTER'
    __table_args__ = {'schema': 'TR'}

    SID = Column(Integer, primary_key=True, autoincrement=True)
    MSGTYPE_SID = Column(Integer, nullable=True)
    MSGDATE = Column(DATETIME, nullable=True)
    MAILBOX_ADDR = Column(NVARCHAR(255), nullable=True)
    EMAILUID = Column(NVARCHAR(50), nullable=True)
    READFLAG = Column(BIT, nullable=True)
    ACTIVE = Column(Integer, nullable=True)  # ควรเปลี่ยนเป็นชนิดข้อมูลที่เหมาะสมสำหรับ ACTIVEFLAG
    SUBJECT = Column(NVARCHAR(1000), nullable=True)
    MSG = Column(NVARCHAR, nullable=True)  # ใช้ NVARCHAR(max) สำหรับข้อความ
    FROMEMAIL = Column(String, nullable=True)  # ควรเปลี่ยนเป็นชนิดข้อมูลที่เหมาะสมสำหรับ EMAIL
    TOEMAIL = Column(NVARCHAR(1000), nullable=True)
    CCEMAIL = Column(NVARCHAR(1000), nullable=True)
    FROMTEL = Column(String, nullable=True)  # ควรเปลี่ยนเป็นชนิดข้อมูลที่เหมาะสมสำหรับ TEL
    TOTEL = Column(String, nullable=True)  # ควรเปลี่ยนเป็นชนิดข้อมูลที่เหมาะสมสำหรับ TEL
    USERS_SID_OWNER = Column(Integer, nullable=True)
    MSGSTATUS_SID = Column(Integer, nullable=True)
    RECCREATE = Column(DATETIME, nullable=True)
    RECUPDATE = Column(DATETIME, nullable=True)
    RECBY = Column(Integer, nullable=True)

    def __str__(self):
        return (f"MsgCenterEntity(SID={self.SID}, MSGTYPE_SID={self.MSGTYPE_SID}, MSGDATE={self.MSGDATE}, "
                f"MAILBOX_ADDR={self.MAILBOX_ADDR}, EMAILUID={self.EMAILUID}, READFLAG={self.READFLAG}, "
                f"ACTIVE={self.ACTIVE}, SUBJECT={self.SUBJECT}, MSG={self.MSG}, "
                f"FROMEMAIL={self.FROMEMAIL}, TOEMAIL={self.TOEMAIL}, CCEMAIL={self.CCEMAIL}, "
                f"FROMTEL={self.FROMTEL}, TOTEL={self.TOTEL}, USERS_SID_OWNER={self.USERS_SID_OWNER}, "
                f"MSGSTATUS_SID={self.MSGSTATUS_SID}, RECCREATE={self.RECCREATE}, "
                f"RECUPDATE={self.RECUPDATE}, RECBY={self.RECBY})")

# Example usage:
# from sqlalchemy import create_engine
# engine = create_engine('mssql+pyodbc://username:password@server/database')
# Base.metadata.create_all(engine)
