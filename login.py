import pyodbc 
import tkinter as tk
from tkinter import ttk

class PassCheck:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.pas=tk.Entry(self.frame, show="*", width=25,  borderwidth=2, relief="groove")
        self.pas.bind('<Return>', self.get_pass)
        self.pas.grid(row=1, column=1, columnspan=1, pady=2)
        self.pas.focus()
        self.frame.pack()
        self.password=""
        self.create_widgets()
    def get_pass (self,a):
        self.password = self.pas.get()
        self.master.destroy()

    def check_pass(self, password, config):
        try:
            with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ password) as conn:
                pass
        except:        
            print("Złe hasło")
            exit()

    def create_widgets(self):

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Konfiguracja", command='')
        self.filemenu.add_command(label="Wyjście", command=self.master.quit)
        self.menubar.add_cascade(label="Opcje", menu=self.filemenu)

        self.master.config(menu=self.menubar)
