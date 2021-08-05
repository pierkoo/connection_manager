import tkinter as tk
from utils import Config
from login import PassCheck
from main_window import MainWindow

def main(): 

    root = tk.Tk()
    #root.geometry("158x24")
    #root.title("Podaj hasło")
    app = PassCheck(root)
    #root.mainloop()
    #password=app.password
    configuration = Config()
    app.check_pass('ppp', configuration)


    root = tk.Tk()
    root.title("Połączenia do klientów")
    root.geometry("575x330")
    app = MainWindow(root,'ppp',configuration)
    root.mainloop()


if __name__ == '__main__':
    main()