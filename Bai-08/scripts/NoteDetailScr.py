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

        self.set_note_data()

        self.btnDong.clicked.connect(self.onButtonDongClicked)

        self.btnLuu.clicked.connect(self.onButtonLuuClicked)

    def onButtonLuuClicked(self):
        # Lấy dữ liệu từ giao diện 
        title = self.lineEditTitle.text()
        content = self.textEditContent.toPlainText()
        
        # Cập nhật lại note ban đầu truyền vào 
        self.note.title = title
        self.note.content = content 

        # Cập nhật cơ sở dữu liệu 
        self.database.update_note(self.note)
        # Tải lại danh sách 
        self.controller.main_window.load_notes()
        # Thông báo ra màn hình 
        QMessageBox.information(self, "Thông báo", "Cập nhật ghi chú thành công!")




    def onButtonDongClicked(self):
        self.close()

    def set_note_data(self):
        self.lineEditTitle.setText(self.note.title)
        self.textEditContent.setText(self.note.content)