import configparser
import pyodbc

class Config():
    path = 'test.ini'
    config = configparser.ConfigParser()
    config.read(path)
    baza = config['BAZA']
    rdp = config['RDP']
    server = ''
    database = ''
    username =''
    rdp_path = ''

    def __init__(self):
        self.server = self.baza.get('server_name') # for a named instance
        self.database =  self.baza.get('database')
        self.username =  self.baza.get('username') 
        self.rdp_path =  self.rdp.get('rdp_path')

    def save_config(self):
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

def check_pass(password, config):
    try:
        with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ password) as conn:
            print("Connected")
            pass
    except:
        print("Wrong password")
        exit()

def save_client_to_db(password,name, contact, info, vpn_name, vpn_login, vpn_pass, rdp_name, rdp_login, rdp_pass, simple_login, simple_pass, rdp_path):
    status = ''
    message = ''
    config = Config()
    with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ password) as conn:

        cursor = conn.cursor()

        zapytanie = f" exec dodaj_klienta '{name}', '{contact}', '{info}', '{vpn_name}', '{vpn_login}', '{vpn_pass}', '{rdp_name}', '{rdp_login}', '{rdp_pass}', '{simple_login}', '{simple_pass}', '{rdp_path}' "
        try:
            cursor.execute(zapytanie)
            message = ''
            status = True
        except pyodbc.Error as err:
            if err.args[0] == '23000':
                message = "Wybrana nazwa juz istnieje w bazie danych!"
            else:
                message = "Nieznany błąd!"
                status = False
    return status, message


