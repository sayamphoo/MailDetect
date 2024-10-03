from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import BIT, DATETIME, NVARCHAR, DATE
from sqlalchemy.orm import relationship

Base = declarative_base()

class RFQHeaderEntity(Base):
    __tablename__ = 'RFQHEADER'
    __table_args__ = {'schema': 'TR'}

    SID = Column(Integer, primary_key=True, autoincrement=True)
    RFQNO = Column(NVARCHAR, nullable=True)
    DUEDATE = Column(DATE, nullable=True)
    PURCHASER_SID = Column(Integer, nullable=True)
    ACTIVE = Column(Integer, nullable=True)  # This depends on the definition of ACTIVEFLAG in your DB
    # SUBMITDATE = Column(DATETIME, nullable=True)
    # FINALAPPROVEDATE = Column(DATETIME, nullable=True)
    # OLDNO = Column(NVARCHAR, nullable=True)
    # GRPREASONSVENDOR = Column(NVARCHAR(500), nullable=True)
    # GRPREASONSAVL = Column(NVARCHAR(500), nullable=True)
    # GRPREASONEDIT = Column(NVARCHAR(500), nullable=True)
    COMPLETE = Column(Integer, nullable=True)  # This depends on the definition of COMPLETEFLAG in your DB
    # COMPLETEREMARK = Column(Text, nullable=True)
    # COMPLETEDATE = Column(DATETIME, nullable=True)
    # POISSUE = Column(BIT, nullable=True)
    # SOURCINGREG_SID = Column(Integer, nullable=True)
    # SOURCINGMETHOD_SID = Column(Integer, nullable=True)
    # STATUS_SID = Column(Integer, nullable=True)
    # RFQTEMP = Column(BIT, nullable=True)
    # RECCREATE = Column(DATETIME, nullable=True)
    # RECUPDATE = Column(DATETIME, nullable=True)
    # RECBY = Column(Integer, nullable=True)
    # POTEXT = Column(Text, nullable=True)
    # TEMPUSER_SID = Column(Integer, nullable=True)
    # RFQTEMPCOMPLETED = Column(BIT, nullable=True)
    # RFQTEMPCOMPLETEDDATE = Column(DATETIME, nullable=True)
    # RFQTEMPPROCESSTIME = Column(Integer, nullable=True)

# Example usage:
# from sqlalchemy import create_engine
# engine = create_engine('mssql+pyodbc://username:password@server/database')
# Base.metadata.create_all(engine)
