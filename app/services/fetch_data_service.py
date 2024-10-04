

from app.repositories.rfq_hearder_repo import RFQHeaderRepository


class DataFetchService:
    def __init__(self):
        pass
    
    def fetch_rfq(self):
        try:
            rfq_header_entity = RFQHeaderRepository().fetch_all(ACTIVE=1, COMPLETE=0)
            return rfq_header_entity
        except Exception as e:
            print(f"Error fetching RFQ headers: {e}")
            return None

    def fetch_mail_vendor(self, rfq_sid, rfq_no):
        try:
            mail_vendor_entity = RFQHeaderRepository().fetch_mail_vendor(rfq_sid, rfq_no)
            return mail_vendor_entity
        except Exception as e:
            print(f"Error fetching mail vendor for RFQ SID {rfq_sid}: {e}")
            return None
