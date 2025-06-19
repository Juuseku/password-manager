from database.connection import DatabaseConnection
import UI.login as log
from psycopg2 import OperationalError
import crypting.crypter as cry
import bcrypt

def main():
    login = log.LoginWindow()
    creds = login.credentials()
    
    try:
        database = DatabaseConnection("localhost", "postgres", creds["db_user"], creds["db_password"], 5433)
        database.initConnection()
        database.createTable()
        database.storeHash(cry.hash_password(creds["master_password"]))
        stored_hash = database.fetchHash()
        if bcrypt.checkpw(creds["master_password"].encode(), stored_hash.encode()):
            print("jes")
        else:
            print("Mee vittuu siitä")

    except OperationalError:
        print("Login Failed")
        exit
    
    


if __name__ == "__main__":
    main()