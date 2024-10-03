from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import NVARCHAR, DATETIME

Base = declarative_base()

class RFQVendorEntity(Base):
    __tablename__ = 'RFQVENDOR'
    __table_args__ = {'schema': 'TR'}

    SID = Column(Integer, primary_key=True, autoincrement=True)
    RFQHEADER_SID = Column(Integer, nullable=True)  # รหัสหัวข้อ RFQ
    COMMONVENDOR_SID = Column(Integer, nullable=True)  # รหัสผู้ขายทั่วไป
    CONTACT = Column(NVARCHAR(255), nullable=True)  # ข้อมูลการติดต่อ
    EMAIL = Column(NVARCHAR(255), nullable=True)  # อีเมล
    FAX = Column(NVARCHAR(255), nullable=True)  # หมายเลขแฟกซ์
    MSGTYPE_SID_ORDERMETHOD = Column(Integer, nullable=True)  # รหัสประเภทข้อความสำหรับวิธีการสั่งซื้อ
    SENTDATE = Column(DATETIME, nullable=True)  # วันที่ส่ง
    ACTIVE = Column(Integer, nullable=True)  # สถานะการใช้งาน
    RECCREATE = Column(DATETIME, nullable=True)  # วันที่สร้างข้อมูล
    RECUPDATE = Column(DATETIME, nullable=True)  # วันที่อัปเดตข้อมูล
    RECBY = Column(Integer, nullable=True)  # รหัสผู้ที่บันทึกข้อมูล
