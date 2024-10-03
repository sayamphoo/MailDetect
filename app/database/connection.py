from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__(self, database_name):
        server_name = "SCC-BSRPDB01"
        driver = "SQL Server"
        trusted_connection = "yes"
        connection_string = f"mssql+pyodbc://{server_name}/{database_name}?driver={driver}&trusted_connection={trusted_connection}"
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        # print("Connection established", database_name)
    
    def get_session(self):
        return self.Session()
    
    def ping(self):
        try:
            session = self.get_session()
            session.execute(text("SELECT 1"))
            print("Ping test successful: Database is reachable.")
        except Exception as e:
            print("Ping test failed:", str(e))
        finally:
            session.close()
