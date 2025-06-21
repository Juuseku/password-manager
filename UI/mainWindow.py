import customtkinter
import crypting.crypter as cry
import database.connection as db

class MainWindow:
    def __init__(self, root, key=None, database=None):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.database = database
        self.root = root
        self.root.geometry("500x275")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.setup_ui()
        self.key = key


    def insert(self):
        if cry.checkExisting(self.entry2.get(), self.database):
            print("already exists")
        else:
            nonce, cipher = cry.encrypt_password(cry.generate_password(), self.key)
            self.database.insertNew(self.entry2.get(), nonce, cipher)
        

    def fetch(self):
        nonce, cipher = self.database.fetchPassword(self.entry1.get())
        pw = cry.decrypt_password(nonce, cipher, self.key)
        print(pw)

    def printAll(self):
        print(self.database.fetchAllSites())

    def setup_ui(self):
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        #Labels
        label_frame = customtkinter.CTkFrame(master=self.frame)
        label_frame.pack(pady=5, padx=10, fill="x")

        label1 = customtkinter.CTkLabel(master=label_frame, text="Fetching", font=("Roboto", 24))
        label1.pack(pady=5, padx=10, side="left")

        label2 = customtkinter.CTkLabel(master=label_frame, text="Storing", font=("Roboto", 24))
        label2.pack(pady=5, padx=10, side="right")

        #Input fields
        entry_frame = customtkinter.CTkFrame(master=self.frame)
        entry_frame.pack(pady=5, padx=10, fill="x")

        fetch_frame = customtkinter.CTkFrame(master=entry_frame)
        fetch_frame.pack(pady=5, padx=10, fill="x", side="left")
        
        self.entry1 = customtkinter.CTkEntry(master=fetch_frame, placeholder_text="Site")
        self.entry1.pack(expand=True)

        store_frame = customtkinter.CTkFrame(master=entry_frame)
        store_frame.pack(pady=5, padx=10, fill="x", side="right")
        
        self.entry2 = customtkinter.CTkEntry(master=store_frame, placeholder_text="Site")
        self.entry2.pack(expand=True)


        #Buttons
        button_frame = customtkinter.CTkFrame(master=self.frame)
        button_frame.pack(pady=5, padx=10, fill="x")

        button1 = customtkinter.CTkButton(master=button_frame, text="Fetch password", command=self.fetch)
        button1.pack(pady=12, side="left", padx=10)

        button2 = customtkinter.CTkButton(master=button_frame, text="Store new password", command=self.insert)
        button2.pack(pady=12, side="right", padx=10)


        #All 'accounts' list
        all_frame = customtkinter.CTkFrame(master=self.frame)
        all_frame.pack(pady=5, padx=10, fill="x")

        button3 = customtkinter.CTkButton(master=all_frame, text="Print all accounts", command=self.printAll)
        button3.pack(pady=12, padx=10)