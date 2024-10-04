from sqlalchemy import desc
from app.models.entities.rfq_hearder_entity import RFQHeaderEntity
from app.repositories.repository import BaseRepository


class RFQHeaderRepository(BaseRepository):
    def __init__(self):
        super().__init__(database_name="SALLY")
        self.query = self.session.query(RFQHeaderEntity)

    def find_by_sid(self, sid):
       return self.query.filter(RFQHeaderEntity.SID == sid).first()
    
    def fetch_all(self,**conditions):
        query =  self.query

        for key, value in conditions.items():
            query = query.filter(getattr(RFQHeaderEntity, key) == value)
            
        
            
        return query.order_by(desc(RFQHeaderEntity.SID)).limit(10).all()