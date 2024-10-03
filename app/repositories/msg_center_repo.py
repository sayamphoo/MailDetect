from app.models.entities.msg_center_entity import MsgCenterEntity
from app.repositories.repository import BaseRepository
from sqlalchemy import func

class MsgCenterRepository(BaseRepository) :
    def __init__(self):
        super().__init__(database_name="SALLY")
        self.query = self.session.query(MsgCenterEntity) 

    def find_by_subject_ilike(self, rfqno):
        return self.query.filter(MsgCenterEntity.SUBJECT.ilike(f"%{rfqno}%")).all()
