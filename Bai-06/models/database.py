from models.note import Note
class Database: 
    def __init__(self): 
        self.notes = []

        note1 = Note("Tiêu đề 1", "Nôi dung 1")
        note2 = Note("Tiêu đề 2", "Nội dung 2")
        note3 = Note("Tiêu đề 3", "Nội dung 3")

        self.notes.append(note1)
        self.notes.append(note2)
        self.notes.append(note3)

    def get_notes(self):
        return self.notes

