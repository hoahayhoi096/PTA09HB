from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic 
import os

class Login(QMainWindow):  
    def __init__(self, controller):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)
        self.mainPage = None

        self.controller = controller

        self.pushButtonDangNhap.clicked.connect(self.onPushButtonDangNhapClicked)


    def onPushButtonDangNhapClicked(self):
        taiKhoan = self.lineEditTaiKhoan.text()
        matKhau = self.lineEditMatKhau.text()

        if taiKhoan == "admin" and matKhau == "123":
            self.controller.show_main_page()
            self.close()
        else :
            QMessageBox.information(self, "Đây là thông báo!", "Đăng nhập thất bại, Vui lòng đăng nhập lại!")
            



