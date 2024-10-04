import re

from app.models.domains.mail import Mail
from app.repositories.msg_center_repo import MsgCenterRepository
from app.repositories.rfq_vendor_repo import RFQVendorRepository
from app.services.detect_mail_service import EmailDetectionService
from app.services.fetch_data_service import DataFetchService



class EmailAnalysisController:
    def __init__(self):
        self.fetch_data_service = DataFetchService()
        self.rfq_vendor_repository = RFQVendorRepository()
        self.msg_center_repository = MsgCenterRepository()
        self.detect_mail_service = EmailDetectionService()

    def analyze_emails(self):
        
        try:
            rfq_headers = self.fetch_data_service.fetch_rfq()
        except Exception as e:
            print(f"Error fetching RFQ headers: {e}")
            return
        
        print(f"Total RFQ Headers: {len(rfq_headers)}\n")
        
        for rfq_header in rfq_headers:
            print("________________________________")
            print("RFQ,SID: ",rfq_header.RFQNO,rfq_header.SID,"\n")
            try:
                rfq_sid = 451023
                rfq_no = "RFQ0450529" 
                # rfq_sid = rfq_header.SID
                # rfq_no = rfq_header.RFQNO
                
                rfq_vendors = self.rfq_vendor_repository.find_by_rfqsid(rfq_sid)
                emails = self.msg_center_repository.find_by_subject_ilike(rfqno=rfq_no)
                
                print("VENDOR",[i.EMAIL for i in rfq_vendors])
                
            except Exception as e:
                print(f"Error fetching vendors or emails for RFQ SID {rfq_sid}: {e}")
                continue

            vendor_emails_list = [re.split(r"[;,]", vendor.EMAIL) for vendor in rfq_vendors]
            for vendor_emails in vendor_emails_list:
                sequent_mail_domain = [
                    Mail(
                        sender=re.split(r"[;,]", email.FROMEMAIL),
                        recipient=re.split(r"[;,]", email.TOEMAIL),
                        cc=re.split(r"[;,]", email.CCEMAIL)
                    )
                    for email in emails
                    if set(vendor_emails) & set(re.split(r"[;,]", email.FROMEMAIL) + re.split(r"[;,]", email.TOEMAIL))
                ]
                
                if sequent_mail_domain :
                    detect_main = EmailDetectionService().detect(sequent_mail_domain)

                 
