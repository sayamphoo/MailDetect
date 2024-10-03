from typing import List

from app.models.domains.mail import Mail
from app.repositories.user_repo import UserRepository


class DetectMailService:
    def __init__(self) -> None:
        self.sender_first_mail: List[str] = []
        self.receive_first_mail: List[str] = []

    def detect(self, email_transactions: List[Mail]):
        self.sender_first_mail = email_transactions[0].sender
        self.receive_first_mail = email_transactions[0].recipient

        if "cposystem@scg.com" == self.sender_first_mail[0] and (
            (
                len(self.receive_first_mail) == 1
                and self.receive_first_mail[0] != "cposystem@scg.com"
            )
            or (len(self.receive_first_mail) > 1)
        ):
            self.__case_one(email_transactions)


    def __case_one(self, email_transactions: List[Mail]):
        
        """
            # Conditions to proceed to case one:
            # 1. The sender is "cposystem@scg.com" AND
            # 2. The number of recipients is 1 AND the single recipient is NOT "cposystem@scg.com"
            # OR
            # 3. The number of recipients is greater than 1 (regardless of the recipient's identity)
        """
        
        print("Case One")
        self.receive_first_mail = [
            email
            for email in self.receive_first_mail
            if email not in self.sender_first_mail
        ]

        for i in email_transactions:
            print("S-> ", i.sender)
            print("R-> ", i.recipient)
            print("C-> ", i.cc)

            if set(i.sender) & set(self.sender_first_mail):
                print("<-- Send \n")
            else:
                print("--> Receive \n")

    def __case_two(self, email_transactions: List[Mail]):
        pass
