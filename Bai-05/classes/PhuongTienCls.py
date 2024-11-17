class PhuongTien:
    def __init__(self, bienso, hangxe, mausac):
        self.bienso = bienso
        self.hangxe = hangxe
        self.mausac = mausac

    def capNhatMauSac(self, mauSacMoi):
        self.mausac = mauSacMoi

    def inThongTin(self):
        print("Biển số:", self.bienso)
        print("Hãng xe:", self.hangxe)
        print("Màu sắc:", self.mausac)


class XeMay(PhuongTien):
    def __init__(self, loaixe, bienso, hangxe, mausac):
        super().__init__(bienso, hangxe, mausac)
        self.loaixe = loaixe

    def display_info(self):
        self.inThongTin()
        print("Loại xe:", self.loaixe)

class Oto(PhuongTien):
    def __init__(self, sochongoi, bienso, hangxe, mausac):
        super().__init__(bienso, hangxe, mausac)
        self.sochongoi = sochongoi

    def display_info(self):
        self.inThongTin()
        print("Loại xe:", self.sochongoi)