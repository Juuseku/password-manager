import customtkinter

class MainWindow:
    def __init__(self, root):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = root
        self.root.geometry("1000x1000")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.setup_ui()


    def insert(self):
        pass

    def setup_ui(self):
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)
        