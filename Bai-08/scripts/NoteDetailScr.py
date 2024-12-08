from PyQt6.QtWidgets import QDialog, QMessageBox, QPushButton
from PyQt6 import uic
import os

class NoteDetail(QDialog):
    def __init__(self,   controller = None, database=None, note = None):
        super().__init__()

        self.setWindowTitle("Note Details")

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/NoteDetail.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = database
        self.note = note

        