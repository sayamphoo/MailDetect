# import re
# from typing import List
# from app.models.domains.mail import Mail
# from app.models.entities.msg_center_entity import MsgCenterEntity
# from app.repositories.msg_center_repo import MsgCenterRepository
# from app.repositories.rfq_hearder_repo import RFQHeaderRepository
# from app.repositories.rfq_vendor_repo import RFQVendorRepository
# from app.services.detect_mail_service import DetectMailService
# from app.services.fetch_data_service import FetchDataService

# if __name__ == "__main__":
#     rfq_headers = FetchDataService().fetch_rfq()
    
#     print(f"Total RFQ Headers: {len(rfq_headers)}\n")
#     for rfq_header in rfq_headers:
#         # rfq_sid = rfq_header.SID
#         # rfq_no = rfq_header.RFQNO
        
#         rfq_sid = 450728
#         rfq_no = "RFQ0450234"

#         print(f"SID: {rfq_sid}, RFQNO: {rfq_no}")

#         rfq_vendors = RFQVendorRepository().find_by_rfqsid(rfq_sid)
#         emails = MsgCenterRepository().find_by_subject_ilike(rfqno=rfq_no)

#         for vendor in rfq_vendors:
#             vendor_emails = re.split(r"[;,]", vendor.EMAIL)
#             print(f"Vendor Emails: {vendor_emails} \n")
            
#             sequent_mail_domain: List[Mail] = []

#             for email in emails:
#                 from_emails = re.split(r"[;,]", email.FROMEMAIL)
#                 to_emails = re.split(r"[;,]", email.TOEMAIL)
#                 cc_emails = re.split(r"[;,]", email.CCEMAIL)
                                
#                 if set(vendor_emails) & set(from_emails + to_emails):
#                     print(f"FROMEMAIL: {from_emails}")
#                     print(f"CCEMAIL: {cc_emails}")
#                     print(f"TOEMAIL: {to_emails}")
#                     sequent_mail_domain.append(
#                         Mail(
#                             sender=from_emails,
#                             recipient=to_emails,
#                             cc=cc_emails,
#                         )
#                     )
            
#             if sequent_mail_domain :
#                 detect_main = DetectMailService().detect(sequent_mail_domain)
                


#                 # Filter emails by comparing vendor_emails with from_emails and to_emails


#             # detect_main = DetectMailService().detect(sequent_mail_domain)

#             # print(detect_main)
#             # print("\n\n")

#         #
#         # print("rfq_vendor_entitys", len(rfq_vendor_entitys))
#         # mail_entitys = MsgCenterRepository().find_by_subject_ilike(rfqno=rfqno)
#         # print("mail_entitys", len(mail_entitys))
#         #
#         # print(rfqhearder.RFQNO)
#         # for i in mail_entitys:
#         #     print("\n")
#         #     print("FROMTEL", i.FROMEMAIL)
#         #     print("CCEMAIL", i.CCEMAIL)
#         #     print("TOEMAIL", i.TOEMAIL)
#         #
#         # print("------------")
#         #
#         # mail_entitys_filtter = [
#         #     i for i in mail_entitys if rfq_vendor_entitys.EMAIL in [i.FROMEMAIL, i.TOEMAIL]
#         # ]
#         #
#         # print(mail_entitys_filtter)
#         #
#         # sequent_mail_domain = [
#         #     (i.FROMEMAIL.split("@")[-1], i.TOEMAIL.split("@")[-1])
#         #     for i in mail_entitys_filtter
#         # ]
#         #
#         # email_transactions = [
#         #     [("a", "g"), "b"],
#         #     [("b", "v"), "g"],
#         #     [("g", "a", "d"), "v"],
#         # ]
#         #
#         # detect_main = DetectMailService().detect(email_transactions)
#         #
#         # print(email_transactions)
#         # print(sequent_mail_domain)
#         # input("_--------> ")

#         # for rfqvendor in rfq_vendor_entitys:
#         #     print("\n\n")
#         #     print(rfqvendor.EMAIL) #ที่จะส่งไป

#         #     mail_entitys_filtter = [i for i in mail_entitys if rfqvendor.EMAIL in [i.FROMEMAIL,i.TOEMAIL]]
#         #     sequent_mail_domain = [(i.FROMEMAIL.split('@')[-1],i.TOEMAIL.split('@')[-1]) for i in mail_entitys_filtter]

#         #     detect_main = DetectMailService().detect(sequent_mail_domain)
#         #     print("----- \n\n")

#         # break


# # def process_email_chain(data):
# #     result = []

# #     for conversation in data:
# #         if isinstance(conversation[0], tuple):
# #             result.append("ส่ง")
# #         else:
# #             result.append("รับ")

# #     return result

# # # ข้อมูลที่ใช้ในการทดสอบ
# # email_data = [
# #     (("a", "g"), "b"),
# #     (("b", "v"), "g"),
# #     (("g", "a", "d"), "v")
# # ]

# # # เรียกฟังก์ชันเพื่อประมวลผล
# # result = process_email_chain(email_data)
# # print(result)


from app.controllers.email_analysis_controller import EmailAnalysisController
from app.repositories.user_repo import UserRepository


if __name__ == "__main__": 
    EmailAnalysisController().analyze_emails()
    
    
    
    # repo = UserRepository()
    # x = repo.find_by_email("suthanyp@scg.com")
    # for i in x:
    #     print(x.SID)