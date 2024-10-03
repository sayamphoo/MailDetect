from app.database.connection import DatabaseConnection


class BaseRepository(DatabaseConnection):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.session = self.get_session()
    
    def close_session(self):
        if self.session:
            self.session.close()