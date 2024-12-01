from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import os

class NoteItem(QWidget):
    def __init__(self, note):
        super().__init__()

        ui_path = os.path.join(os.path.dirname(__file__), "../UI/NoteItem.ui")
        uic.loadUi(ui_path, self)

        self.labelTitle.setText(note.title)
        self.labelContent.setText(note.content)
        
