from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os

from scripts.MainPageScr import MainPage

class Login(QMainWindow):  
    def __init__(self):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)
        self.mainPage = None

        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhapClicked)


    def onPushButtonDangNhapClicked(self):
        taiKhoan = self.lineEditTaiKhoan.text()
        matKhau = self.lineEditMatKhau.text()

        if taiKhoan == "admin" and matKhau == "123":
            self.mainPage = MainPage()
            self.mainPage.show()
            self.close()
        else :
            QMessageBox.information(self, "Đây là thông báo!", "Đăng nhập thất bại, Vui lòng đăng nhập lại!")
            



