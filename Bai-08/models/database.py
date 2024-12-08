from models.note import Note
class Database: 
    def __init__(self): 
        self.notes = []

        note1 = Note("Tiêu đề 1", "Nôi dung 1")
        note2 = Note("Tiêu đề 2", "Nội dung 2")
        note3 = Note("Tiêu đề 3", "Nội dung 3")
        note4 = Note("Tiêu đề 4", "Nội dung 4")

        self.notes.append(note1)
        self.notes.append(note2)
        self.notes.append(note3)
        self.notes.append(note4)

    def update_note(self, note):
        for item in self.notes:
            if item.id == note.id:
                item.title = note.title
                item.content = note.content


    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def get_notes(self):
        return self.notes
    
    def add_note(self, new_note):
        self.notes.append(new_note)

