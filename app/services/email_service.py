import re
from app.models.domains.mail import Mail


class EmailService:
    def __init__(self, msg_center_repository: MsgCenterRepository):
        self.msg_center_repository = msg_center_repository

    def get_emails_by_rfq(self, rfq_no):
        return self.msg_center_repository.find_by_subject_ilike(rfqno=rfq_no)

    def filter_vendor_emails(self, emails, vendor_emails):
        sequent_mail_domain = [
            Mail(
                sender=re.split(r"[;,]", email.FROMEMAIL),
                recipient=re.split(r"[;,]", email.TOEMAIL),
                cc=re.split(r"[;,]", email.CCEMAIL)
            )
            for email in emails
            if set(vendor_emails) & set(re.split(r"[;,]", email.FROMEMAIL) + re.split(r"[;,]", email.TOEMAIL))
        ]
        return sequent_mail_domain
