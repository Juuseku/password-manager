import psycopg2


class DatabaseConnection:
    def __init__(self, host: str, name: str, user: str, password: str, port: int):
        self.__host = host
        self.__dbname = name
        self.__user = user
        self.__pw = password
        self.__port = port
        self.__conn = None
        self.__cur = None

    def initConnection(self):
        self.__conn = psycopg2.connect(host=self.__host, dbname=self.__dbname, user=self.__user, password=self.__pw, port=self.__port)
        self.__cur = self.__conn.cursor()

    def createTable(self):
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS pws (
                    site VARCHAR(255),
                    password VARCHAR(255)
                    );
                """)
        self.__conn.commit()

    def storeHash(self, hash:str):
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS master_password (
            id SERIAL PRIMARY KEY,
            password_hash BYTEA NOT NULL       
            );        
        """)
        self.__cur.execute("""SELECT COUNT(*) FROM master_password;""")
        count = self.__cur.fetchone()[0]

        if count > 0:
            raise Exception("Master password already set.")
        
        self.__cur.execute("""INSERT INTO master_password (password_hash) VALUES (%s);""", (hash,))
        self.__conn.commit()

    def fetchHash(self):
        self.__cur.execute("""SELECT password_hash FROM master_password LIMIT 1;""")
        stored_hash = self.__cur.fetchone()[0]
        return stored_hash

    def insertNew(site: str, pw: str):
        pass

    def closeConnection(self):
        self.__cur.close()
        self.__conn.close()