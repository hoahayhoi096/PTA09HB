from PyQt6.QtWidgets import QMainWindow
import sys
from PyQt6 import uic 
import os

class Login(QMainWindow):  
    def __init__(self):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/Login.ui")
        uic.loadUi(ui_path, self)

