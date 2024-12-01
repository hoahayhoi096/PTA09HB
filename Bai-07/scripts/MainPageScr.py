from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6.QtCore import QSize
import sys
from PyQt6 import uic 
import os
from scripts.NoteItemScr import NoteItem
from scripts.AddNoteScr import AddNote

class MainPage(QMainWindow):  
    def __init__(self, controller, database):
        super().__init__()

        # Tải các thành phần giao diện 
        ui_path = os.path.join(os.path.dirname(__file__), "../UI/MainPage.ui")
        uic.loadUi(ui_path, self)

        self.controller = controller
        self.database = database

        self.load_notes()

        # Mở cửa sổ/ trang thêm ghi chú
        self.pushButtonAdd.clicked.connect(self.onPushButtonAdd)
        self.AddNoteWindow = AddNote(self.database, self.controller)


    def load_notes(self):
        self.listWidget.clear()
        self.listWidget.setSpacing(10)

        ds_note = self.database.get_notes()
        
        for note in ds_note: 
            noteWidget = NoteItem(note)

            item = QListWidgetItem(self.listWidget)

            noteWidget.setFixedSize(500, 120)

            item.setSizeHint(QSize(500, 120))

            self.listWidget.addItem(item)

            self.listWidget.setItemWidget(item, noteWidget)


    def onPushButtonAdd(self):
        self.AddNoteWindow.show()
        



        