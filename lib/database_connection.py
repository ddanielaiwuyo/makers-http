import psycopg
from psycopg.rows import dict_row

class DatabaseConnection:
    
    def connect(self, database_name=None):
        DEFAULT_DB = "http_challenge_1"
        if database_name is None:
            print("\n [warning] database_name was not provided, using default", DEFAULT_DB)
            database_name = DEFAULT_DB

        connstr = f"postgresql://localhost/{database_name}"
        try:
            self.conn = psycopg.connect(connstr, row_factory=dict_row)

            print("connection established successfully with database")
        except psycopg.OperationalError as err:
            raise psycopg.OperationalError(err)
    

    def seed(self, seed_path=None):
        DEFAULT_SEED_PATH = "seeds/http_challenge_1.sql"
        if seed_path is None:
            print("\n [warning] seed path was not provided,  using default", DEFAULT_SEED_PATH)
            seed_path = DEFAULT_SEED_PATH

        file_content = ""
        with open(seed_path, "r") as f:
            file_content = f.read()

        self._check_conn()
        with self.conn.cursor() as cursor:
            cursor.execute(file_content)

            self.conn.commit()

    def execute(self, query, params=None):
        self._check_conn()

        results = []
        try:
            with self.conn.cursor() as cursor:
                if params is None:
                    params = []
                response = cursor.execute(query, params)
                if cursor.description is None:
                    results = None
                else:
                    results = response.fetchall()

                self.conn.commit()

            return results
        except Exception:
            import traceback
            traceback.print_exc()

    def _check_conn(self):
        err_msg = """ 
        Connection with the database has been nullified
        Either database has gone off, or has been disconnected
        please check!
        """
        if self.conn is None:
            raise Exception(err_msg)

            

def main():
    db = DatabaseConnection()
    db.connect()
    db.seed()

if __name__ == "__main__":
    main()
    
