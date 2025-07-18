from database.connection import DatabaseConnection
from UI.login import LoginWindow
from UI.mainWindow import MainWindow
from psycopg2 import OperationalError
import crypting.crypter as cry
import bcrypt
import customtkinter

def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.geometry("500x350")
    
    db_instance = {}
    key = {}
    salt = None
    
    def handle_login(creds, app):
        try:
            database = DatabaseConnection("localhost", "postgres", creds["db_user"], creds["db_password"], 5433)
            database.initConnection()
            database.createTable()
            database.storeHash(cry.hash_password(creds["master_password"]))
            database.storeSalt(cry.generate_salt())
            stored_hash = database.fetchHash()
            salt = bytes(database.fetchSalt())

            if bcrypt.checkpw(creds["master_password"].encode(), bytes(stored_hash)):
                db_instance['db'] = database
                key['key'] = cry.derive_key(creds["master_password"], salt)
                app.authenticationSuccesfull()
            else:
                print("Mee vittuu siitä")

        except OperationalError:
            print("Login Failed")
            exit
    
    LoginWindow(root, switch=lambda: MainWindow(root, key['key'], db_instance['db']),  handle_login=handle_login)
    root.mainloop()
    


if __name__ == "__main__":
    main()