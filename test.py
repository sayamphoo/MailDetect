import unittest
from app.repositories.user_repo import UserRepository

class TestRepo(unittest.TestCase) :
    def test_user(self) :
        repo = UserRepository()
        print(repo.is_email_for_pb("suthanyp@scg.com"))
    
    
if __name__ == '__main__':
   unittest.main()