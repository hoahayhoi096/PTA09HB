from PyQt6.QtWidgets import QApplication, QWidget
import sys
from scripts.LoginScr import Login
from scripts.MainPageScr import MainPage
from models.database import Database

class Controller: 
    def __init__(self):
        # Khởi tạo dữ liệu 
        self.db = Database()

        #Khởi tạo tác cửa sổ 
        self.main_window = MainPage(self, self.db)
        self.login_window = Login(self)

    def show_main_page(self):
        self.main_window.show()

    def show_login_page(self):
        self.login_window.show()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    app.exec()


