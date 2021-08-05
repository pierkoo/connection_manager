import configparser

class Config():

    config = configparser.ConfigParser()
    config.read('test.ini')
    baza = config['BAZA']
    server = ''
    database = ''
    username =''

    def __init__(self):
        self.server = self.baza.get('server_name') # for a named instance
        self.database =  self.baza.get('database')
        self.username =  self.baza.get('username') 