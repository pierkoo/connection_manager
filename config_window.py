import pyodbc
import tkinter as tk
from tkinter import ttk
from utils import Config

class ConfigurationWindow:

    def __init__(self,master):
        self.master = master
        self.master.wm_attributes("-disabled", True)

        self.top=tk.Toplevel(master)
        self.top.geometry('500x130')

        lab_width = 12
        txt_width = 20
        but_width = 20

        self.top_label = tk.Label(self.top, text="Serwer:")
        self.top_label.grid(row=1, column=1, sticky=tk.W)
        self.top_label.config(width=lab_width)
        self.top_label2 = tk.Label(self.top, text="Baza:")
        self.top_label2.grid(row=2, column=1, sticky=tk.W)
        self.top_label2.config(width=lab_width)
        self.top_label3 = tk.Label(self.top, text="Login:")
        self.top_label3.grid(row=3, column=1, sticky=tk.W)
        self.top_label3.config(width=lab_width)

        self.top_label4 = tk.Label(self.top, text="Folder RDP:")
        self.top_label4.grid(row=4, column=1, sticky=tk.W)
        self.top_label4.config(width=lab_width)

        self.text1 = tk.Entry(self.top, width=20)
        self.text1.grid(row=1, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5)
        self.text1.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.text2 = tk.Entry(self.top, width=20)
        self.text2.grid(row=2, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5)
        self.text2.configure(font='Calibri 12', borderwidth=2, relief="groove")

        self.text3 = tk.Entry(self.top,  width=20)
        self.text3.grid(row=3, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5)
        self.text3.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.text4 = tk.Entry(self.top,  width=40)
        self.text4.grid(row=4, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5)
        self.text4.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.save_button = tk.Button(self.top, text="Zapisz",  bg = '#ffcccc',  command= lambda: self.save_config())
        self.save_button.grid(row=5, column=1, sticky=tk.W)
        self.save_button.config(width=but_width)

        self.cancel_button = tk.Button(self.top, text="Anuluj",  bg = '#ffcccc', command= lambda: self.close_window())
        self.cancel_button.grid(row=5, column=2, sticky=tk.W)
        self.cancel_button.config(width=but_width)


        self.config = Config()
        self.text1.insert(tk.INSERT,self.config.server)
        self.text2.insert(tk.INSERT,self.config.database)
        self.text3.insert(tk.INSERT,self.config.username)
        self.text4.insert(tk.INSERT,self.config.rdp_path)



        self.top.protocol("WM_DELETE_WINDOW", self.close_window)

    def save_config(self):

        self.config.config['BAZA']['server_name']= self.text1.get()
        self.config.config['BAZA']['database']= self.text2.get()
        self.config.config['BAZA']['username']= self.text3.get()
        self.config.config['RDP']['rdp_path']= self.text4.get()
        self.config.save_config()
        self.close_window()

    def close_window(self):
        self.master.wm_attributes("-disabled", False)
        self.top.destroy()
