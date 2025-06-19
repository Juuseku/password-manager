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
    root.geometry("750x1000")
    
    
    def handle_login(creds, app):
        try:
            database = DatabaseConnection("localhost", "postgres", creds["db_user"], creds["db_password"], 5433)
            database.initConnection()
            database.createTable()
            database.storeHash(cry.hash_password(creds["master_password"]))
            stored_hash = database.fetchHash()

            if bcrypt.checkpw(creds["master_password"].encode(), bytes(stored_hash)):
                app.authenticationSuccesfull()
            else:
                print("Mee vittuu siitä")

        except OperationalError:
            print("Login Failed")
            exit
    
    LoginWindow(root, switch=lambda: MainWindow(root), handle_login=handle_login)
    root.mainloop()
    


if __name__ == "__main__":
    main()