from app.models.entities.user_entity import UserEntity
from app.repositories.repository import BaseRepository


class UserRepository(BaseRepository) :
    def __init__(self):
        super().__init__(database_name="SALLY")
        self.query = self.session.query(UserEntity)

    # def find_by_email(self, email) -> UserEntity:
    #     return self.query.filter(UserEntity.EMAIL == email).first()
    
    def is_email_for_pb(self, email):
        return self.query.filter(UserEntity.EMAIL == email).first() is not None