from app.models.entities.rfq_vendor_entity import RFQVendorEntity
from app.repositories.repository import BaseRepository


class RFQVendorRepository(BaseRepository) : 
    def __init__(self):
        super().__init__(database_name="SALLY")
        self.query = self.session.query(RFQVendorEntity)

    def find_by_rfqsid(self, rfqsid):
        return self.query.filter(RFQVendorEntity.RFQHEADER_SID == rfqsid).all()