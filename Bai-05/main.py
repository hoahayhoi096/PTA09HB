from PyQt6.QtWidgets import QApplication, QWidget
import sys
from scripts.LoginScr import Login

app = QApplication(sys.argv)

window = Login()

window.show()
app.exec()