import customtkinter
import getpass

class LoginWindow:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.results = None

        self.setup_ui()
        self.root.mainloop()

    def login(self):
        self.results = {
            "db_user": self.entry1.get(),
            "master_password": self.entry2.get(),
            "db_password": self.entry3.get()
        }
        self.root.destroy()

    def setup_ui(self):
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="DB password", show="*")
        self.entry3.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=frame, text="Login", command=self.login)
        button.pack(pady=12, padx=10)

    def credentials(self):
        return self.results

        
