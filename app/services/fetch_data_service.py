from app.repositories.rfq_hearder_repo import RFQHeaderRepository


class FetchDataService() :
    def __init__(self):
        pass
    
    def fetch_rfq(self):
        rfq_hearder_entity = RFQHeaderRepository().fetch_all(ACTIVE=1,COMPLETE=0)
        return rfq_hearder_entity
    
    def fetch_mail_vendor(self, rfq_sid, rfq_no):
        mail_vendor_entity = RFQHeaderRepository().fetch_mail_vendor(rfq_sid, rfq_no)
        
        # return mail_vendor_entity
    
    