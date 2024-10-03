from dataclasses import dataclass, field
from typing import List

@dataclass
class Mail:
    sender: List[str] = field(default_factory=list)
    recipient: List[str] = field(default_factory=list)
    cc: List[str] = field(default_factory=list)
    subject: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.sender or not self.recipient:
            raise ValueError("Sender and recipient cannot be empty.")

    def display(self):
        cc_list = ', '.join(self.cc) if self.cc else 'None'
        return f"From: {self.sender}\nTo: {self.recipient}\nCc: {cc_list}\nSubject: {self.subject}"
