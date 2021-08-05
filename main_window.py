import pyodbc 
from datetime import datetime
import subprocess
import tkinter as tk
from tkinter import ttk
import pyperclip
import os

class MainWindow:
    
    def __init__(self, master,password, config):
        self.server = config.server # for a named instance
        self.database = config.database
        self.username = config.username
        self.data={"Nazwa":"",
                    "Info":"",
                    "Kontakt":"",
                    "VPN_Info":"",
                    "VPN_login":"",
                    "VPN_pass":"",
                    "RDP_Info":"",
                    "RDP_login":"",
                    "RPD_pass":"",
                    "Simple_login":"",
                    "Simple_pass":"",
                    "RDP_path":""
                   }

        self.password=password
        self.master = master
        self.frame = tk.Frame(self.master)
        self.nazwa_all = self.get_list()
        self.create_widgets()

    def create_widgets(self):

        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)

        self.filemenu.add_command(label="Dodaj klienta", command='')
        self.filemenu.add_command(label="Edytuj klienta", command='')
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Konfiguracja", command='')
        self.filemenu.add_command(label="Wyjście", command=self.master.quit)
        self.menubar.add_cascade(label="Opcje", menu=self.filemenu)

        self.master.config(menu=self.menubar)

        lab_width = 12
        txt_width = 20
        but_width = 20

        self.lab_nazwa = tk.Label(self.frame, text="Klient")
        self.lab_nazwa.grid(row=1, column=1, sticky=tk.E)
        self.lab_nazwa.config(width=lab_width)

        self.lista = ttk.Combobox(self.frame, values=self.nazwa_all)
        self.lista.bind("<<ComboboxSelected>>", self.get_data)
        self.lista.grid(row=1, column=2, columnspan=2, sticky=tk.W, pady=5)

        self.text = tk.Text(self.frame, height=15, width=50)
        self.text.grid(row=2, column=1, sticky=tk.W, columnspan=2, rowspan=10, padx=5)
        self.text.configure(font='Calibri 12', wrap=tk.WORD, borderwidth=2, relief="groove")

        # self.lab_vpn = tk.Label(self.frame, text="VPN")
        # self.lab_vpn.grid(row=3, column=3, sticky=tk.W)
        # self.lab_vpn.config(width=lab_width)

        # self.lab_rdp=tk.Label(self.frame, text="RDP")
        # self.lab_rdp.grid(row=7, column=3, sticky=tk.W)
        # self.lab_rdp.config(width=lab_width)

        # self.lab_simple = tk.Label(self.frame, text="Simple")
        # self.lab_simple.grid(row=11, column=3, sticky=tk.W)
        # self.lab_simple.config(width=lab_width)
        
        self.but_vpn_info = tk.Button(self.frame, text="VPN Info",  bg = '#ffcccc')
        self.but_vpn_info.grid(row=3, column=3, sticky=tk.W)
        self.but_vpn_info.config(width=but_width)
        
        self.but_vpn_login= tk.Button(self.frame, text="VPN Login", bg = '#ffcccc', command= lambda: self.copy_password(str(self.data["VPN_login"])))
        self.but_vpn_login.grid(row=4, column=3, sticky=tk.W)
        self.but_vpn_login.config(width=but_width)

        self.but_vpn_pass = tk.Button(self.frame, text="VPN Pass", bg = '#ffcccc', command= lambda: self.copy_password(str(self.data["VPN_pass"])))
        self.but_vpn_pass.grid(row=5, column=3, sticky=tk.W)
        self.but_vpn_pass.config(width=but_width)

        self.but_rdp_info = tk.Button(self.frame, text="Start RDP", command=self.start_rdp, bg='#ccffcc')
        self.but_rdp_info.grid(row=6, column=3, sticky=tk.W)
        self.but_rdp_info.config(width=but_width)

        self.but_rdp_login= tk.Button(self.frame, text="RDP Login", bg = '#ccffcc', command= lambda: self.copy_password(str(self.data["RDP_login"])))
        self.but_rdp_login.grid(row=7, column=3, sticky=tk.W)
        self.but_rdp_login.config(width=but_width)

        self.but_rdp_pass = tk.Button(self.frame, text="RDP Pass", bg = '#ccffcc', command= lambda: self.copy_password(str(self.data["RPD_pass"])))
        self.but_rdp_pass.grid(row=8, column=3, sticky=tk.W)
        self.but_rdp_pass.config(width=but_width)

        self.but_simple_login= tk.Button(self.frame, text="Simple Login", bg = '#66ccff', command= lambda: self.copy_password(str(self.data["Simple_login"])))
        self.but_simple_login.grid(row=9, column=3, sticky=tk.W)
        self.but_simple_login.config(width=but_width)

        self.but_simple_pass = tk.Button(self.frame, text="Simple Pass", bg = '#66ccff', command= lambda: self.copy_password(str(self.data["Simple_pass"])))
        self.but_simple_pass.grid(row=10, column=3, sticky=tk.W)
        self.but_simple_pass.config(width=but_width)

        self.frame.pack()

    def get_list(self):
        with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password) as conn:
            cursor = conn.cursor()
            zapytanie = " select nazwa from klient "
            cursor.execute(zapytanie)
            rows = cursor.fetchall()
            nazwa_all = [row[0] for row in rows ]
            return nazwa_all

    def get_data(self,a):
        with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password) as conn:
            cursor = conn.cursor()
            zapytanie = " select * from klient where nazwa like '" + self.lista.get() + "'"
            cursor.execute(zapytanie)
            row = cursor.fetchone()

            self.text.delete(1.0, tk.END)

            i=0
            for e in self.data:
                self.data[e]=row[i]
                i+=1

            self.text.insert(tk.INSERT,"Nazwa"+ " - " +str(self.data["Nazwa"])+"\n\n")
            self.text.insert(tk.INSERT,"Info"+ " - " +str(self.data["Info"])+"\n\n")
            self.text.insert(tk.INSERT,"kontakt"+ " - " +str(self.data["Kontakt"])+"\n")


            self.but_vpn_info.config( text= str(self.data["VPN_Info"]))

            self.but_vpn_login.config( text= str(self.data["VPN_login"]))

            self.but_vpn_pass.config(text= "***")

            self.but_rdp_info.config( text= str(self.data["RDP_Info"]))

            self.but_rdp_login.config( text= str(self.data["RDP_login"]))

            self.but_rdp_pass.config( text= "***")

            self.but_simple_login.config( text= str(self.data["Simple_login"]))
  
            self.but_simple_pass.config( text= "***")

    def copy_password(self,h):
        pyperclip.copy(h)

    def start_rdp(self):
        
        if str(self.data["RDP_path"]) != "None" and str(self.data["RDP_path"]) != "" :
            os.startfile(str(self.data["RDP_path"]))
        else:
             os.startfile("C:/Users/pszlaski/Documents/MOJE/Połączenia")
