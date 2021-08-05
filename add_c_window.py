import pyodbc
import tkinter as tk
from tkinter import ttk, messagebox
from utils import save_client_to_db



class AddClientWindow:

    def __init__(self,master, password):
        self.password = password
        self.master = master
        self.master.wm_attributes("-disabled", True)

        self.top=tk.Toplevel(master)
        self.top.title("Nowy klient")
        self.top.geometry('440x430')

        lab_width = 12
        txt_width = 40
        but_width = 10

        self.l_client_name = tk.Label(self.top, text="Nazwa:")
        self.l_client_name.grid(row=1, column=1, sticky=tk.W)
        self.l_client_name.config(width=lab_width)

        self.l_contact = tk.Label(self.top, text="Kontakt:")
        self.l_contact.grid(row=2, column=1, sticky=tk.W)
        self.l_contact.config(width=lab_width)

        self.l_info = tk.Label(self.top, text="Info:")
        self.l_info.grid(row=4, column=1, sticky=tk.W)
        self.l_info.config(width=lab_width)

        self.l_vpn_name = tk.Label(self.top, text="VPN:")
        self.l_vpn_name.grid(row=7, column=1, sticky=tk.W)
        self.l_vpn_name.config(width=lab_width)

        self.l_vpn_login = tk.Label(self.top, text="VPN Login:")
        self.l_vpn_login.grid(row=8, column=1, sticky=tk.W)
        self.l_vpn_login.config(width=lab_width)

        self.l_vpn_pass = tk.Label(self.top, text="VPN Pass:")
        self.l_vpn_pass.grid(row=9, column=1, sticky=tk.W)
        self.l_vpn_pass.config(width=lab_width)

        self.l_rdp_name = tk.Label(self.top, text="RDP:")
        self.l_rdp_name.grid(row=10, column=1, sticky=tk.W)
        self.l_rdp_name.config(width=lab_width)

        self.l_rdp_login = tk.Label(self.top, text="RDP Login:")
        self.l_rdp_login.grid(row=11, column=1, sticky=tk.W)
        self.l_rdp_login.config(width=lab_width)

        self.l_rdp_pass = tk.Label(self.top, text="RDP Pass:")
        self.l_rdp_pass.grid(row=12, column=1, sticky=tk.W)
        self.l_rdp_pass.config(width=lab_width)

        self.l_simple_login = tk.Label(self.top, text="Simple Login:")
        self.l_simple_login.grid(row=13, column=1, sticky=tk.W)
        self.l_simple_login.config(width=lab_width)

        self.l_simple_pass = tk.Label(self.top, text="Simple Pass:")
        self.l_simple_pass.grid(row=14, column=1, sticky=tk.W)
        self.l_simple_pass.config(width=lab_width)

        #### ENTRIES

        self.e_client_name = tk.Entry(self.top, width=txt_width)
        self.e_client_name.grid(row=1, column=2, sticky=tk.S, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_client_name.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_contact = tk.Text(self.top, width=txt_width, height=2)
        self.e_contact.grid(row=2, column=2, sticky=tk.W, columnspan=2, rowspan=2, padx=5, pady=2)
        self.e_contact.configure(font='Calibri 12',  borderwidth=2, relief="groove")
        self.e_contact.bind("<Tab>", self.focus_next_widget)

        self.e_info = tk.Text(self.top, width=txt_width, height=3)
        self.e_info.grid(row=4, column=2, sticky=tk.W, columnspan=2, rowspan=3, padx=5, pady=2)
        self.e_info.configure(font='Calibri 12',  borderwidth=2, relief="groove")
        self.e_info.bind("<Tab>", self.focus_next_widget)

        self.e_vpn_name = tk.Entry(self.top, width=txt_width)
        self.e_vpn_name.grid(row=7, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_vpn_name.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_vpn_login = tk.Entry(self.top, width=txt_width)
        self.e_vpn_login.grid(row=8, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_vpn_login.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_vpn_pass = tk.Entry(self.top, width=txt_width)
        self.e_vpn_pass.grid(row=9, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_vpn_pass.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_rdp_name = tk.Entry(self.top, width=txt_width)
        self.e_rdp_name.grid(row=10, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_rdp_name.configure(font='Calibri 12', borderwidth=2, relief="groove")

        self.e_rdp_login = tk.Entry(self.top, width=txt_width)
        self.e_rdp_login.grid(row=11, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_rdp_login.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_rdp_pass = tk.Entry(self.top, width=txt_width)
        self.e_rdp_pass.grid(row=12, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_rdp_pass.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_simple_login = tk.Entry(self.top, width=txt_width)
        self.e_simple_login.grid(row=13, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_simple_login.configure(font='Calibri 12',  borderwidth=2, relief="groove")

        self.e_simple_pass = tk.Entry(self.top, width=txt_width)
        self.e_simple_pass.grid(row=14, column=2, sticky=tk.W, columnspan=2, rowspan=1, padx=5, pady=2)
        self.e_simple_pass.configure(font='Calibri 12',  borderwidth=2, relief="groove")



        self.save_button = tk.Button(self.top, text="Zapisz",  bg = '#ccffcc',  command= lambda: self.save_client())
        self.save_button.grid(row=15, column=2, sticky=tk.W, padx=5, pady=20)
        self.save_button.config(width=but_width)

        self.cancel_button = tk.Button(self.top, text="Anuluj",  bg = '#ffcccc', command= lambda: self.close_window())
        self.cancel_button.grid(row=15, column=3, sticky=tk.W, padx=5, pady=20)
        self.cancel_button.config(width=but_width)





        self.top.protocol("WM_DELETE_WINDOW", self.close_window)

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def save_client(self):
        if self.e_client_name.get():

            status, message = save_client_to_db(self.password,
                self.e_client_name.get(),
                self.e_info.get("1.0","end-1c"),
                self.e_contact.get("1.0","end-1c"),
                self.e_vpn_name.get(),
                self.e_vpn_login.get(),
                self.e_vpn_pass.get(),
                self.e_rdp_name.get(),
                self.e_rdp_login.get(),
                self.e_rdp_pass.get(),
                self.e_simple_login.get(),
                self.e_simple_pass.get(),
                "rdp_path")

            if status:
                self.master.wm_attributes("-disabled", False)
                self.top.destroy()
            else:
                messagebox.showwarning(title="Błąd podczas zapisu", message=message)

        else:
            messagebox.showwarning(title="Brak nazwy klienta", message="Przed zapisaniem podaj nazwę klienta")


    def close_window(self):
        self.master.wm_attributes("-disabled", False)
        self.top.destroy()
