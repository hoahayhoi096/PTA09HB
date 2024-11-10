class DongVat:
    def __init__(self, ten, tuoi, loai, moitruongsong):
        self.ten = ten 
        self.tuoi = tuoi 
        self.loai = loai 
        self.moitruongsong = moitruongsong

    def capNhatMoiTrongSong(self, moiTruongSongMoi):
        self.moitruongsong = moiTruongSongMoi

    def inThongTin(self):
        print("Tên động vật:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Loài:", self.loai)
        print("Mồi trường sống:", self.moitruongsong)
