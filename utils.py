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


def delete_client_from_db(password,name,callback):
    config = Config()
    with pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ password) as conn:
        cursor = conn.cursor()
        zapytanie = f"delete from klient where nazwa = '{name}' "
        try:
            cursor.execute(zapytanie)
            message = ''
            status = True

        except pyodbc.Error as err:
            message = "Nieznany błąd!"
            status = False

    callback()
    return status, message

def create_rdp_file(path,ip,login):
    rdp_text = f'''screen mode id:i:2
                    use multimon:i:0
                    desktopwidth:i:800
                    desktopheight:i:600
                    session bpp:i:32
                    winposstr:s:0,3,0,0,800,600
                    compression:i:1
                    keyboardhook:i:2
                    audiocapturemode:i:0
                    videoplaybackmode:i:1
                    connection type:i:7
                    networkautodetect:i:1
                    bandwidthautodetect:i:1
                    displayconnectionbar:i:1
                    username:s:{login}
                    enableworkspacereconnect:i:0
                    disable wallpaper:i:0
                    allow font smoothing:i:0
                    allow desktop composition:i:0
                    disable full window drag:i:1
                    disable menu anims:i:1
                    disable themes:i:0
                    disable cursor setting:i:0
                    bitmapcachepersistenable:i:1
                    full address:s:{ip}
                    audiomode:i:0
                    redirectprinters:i:1
                    redirectcomports:i:0
                    redirectsmartcards:i:1
                    redirectclipboard:i:1
                    redirectposdevices:i:0
                    autoreconnection enabled:i:1
                    authentication level:i:2
                    prompt for credentials:i:0
                    negotiate security layer:i:1
                    remoteapplicationmode:i:0
                    alternate shell:s:
                    shell working directory:s:
                    gatewayhostname:s:
                    gatewayusagemethod:i:4
                    gatewaycredentialssource:i:4
                    gatewayprofileusagemethod:i:0
                    promptcredentialonce:i:0
                    gatewaybrokeringtype:i:0
                    use redirection server name:i:0
                    rdgiskdcproxy:i:0
                    kdcproxyname:s:'''
    with open("TEST.rdp", "w") as file:
        file.write(rdp_text)




