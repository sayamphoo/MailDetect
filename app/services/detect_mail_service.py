from typing import List
from app.models.domains.mail import Mail
from app.repositories.user_repo import UserRepository


class EmailDetectionService:
    def __init__(self) -> None:
        self.sender_first_mail: List[str] = []
        self.receive_first_mail: List[str] = []
        self.user_repository: UserRepository = UserRepository()

    def detect(self, email_transactions: List[Mail]):
        self.sender_first_mail = email_transactions[0].sender
        self.receive_first_mail = email_transactions[0].recipient

        if self.__is_normal_case():
            self.__normal_case(email_transactions)
        elif self.__is_exception_one_case():
            self.__exception_one_case(email_transactions)

    def _normal_case(self, email_transactions: List[Mail]) -> List[str]:
        """
            Conditions to proceed to case one:
            1. The sender is "cposystem@scg.com" AND
            2. The number of recipients is 1 AND the single recipient is NOT "cposystem@scg.com"
            OR
            3. The number of recipients is greater than 1 (regardless of the recipient's identity)
        """
        print("Case One")

        result = []
        
        
        # Delect ตัวที่เหมือน Sender // Delect ข้อมูลที่ส่งหาตัวเอง
        
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
                print("|<-- Send\n")
                result.append("Send")
            elif set(i.sender) & set(self.receive_first_mail):
                print("|--> Receive\n")
                result.append("Receive")
            else:
                print("incident\n")
        
        return result

    def _exception_one_case(self, email_transactions: List[Mail]):
        """
           Conditions to proceed to Exception one case
           
           1. Do the same as def normal case, sent email by pb
                but email cc cposystem@scg.com
        """
        print("exception_one_case")
        
        result = []

        self.receive_first_mail = [
            email
            for email in self.receive_first_mail
            if email not in self.sender_first_mail
        ]

        for i in email_transactions:
            print("S-> ", i.sender)
            print("R-> ", i.recipient)
            print("C-> ", i.cc)

            if set(i.sender) & set(self.sender_first_mail) & set(i.cc):
                print("|<-- Send\n")
                result.append("Send")
            elif set(i.sender) & set(self.receive_first_mail) & set(i.cc):
                print("|--> Receive\n")
                result.append("Receive")
            else:
                print("incident\n")
        
        return result

    def __is_normal_case(self) -> bool:
        return self.sender_first_mail[0] == "cposystem@scg.com" and (
            len(self.receive_first_mail) == 1
            and self.receive_first_mail[0] != "cposystem@scg.com"
            or len(self.receive_first_mail) > 1
        )

    def __is_exception_one_case(self) -> bool:
        return (
            self.sender_first_mail[0].endswith( "@scg.com" ) \
                and self.user_repository.is_email_for_pb(self.sender_first_mail[0]) \
                and self.receive_first_mail[0] != "cposystem@scg.com"
        )
        
    def __is_exception_two_case(self) -> bool :
        return True