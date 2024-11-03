class ConNguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi 

    def doiTen(self, tenMoi):
        self.ten = tenMoi

    def capNhatTuoi(self, tuoiMoi):
        self.tuoi = tuoiMoi

class HocSinh(ConNguoi):
    def __init__(self, ten, tuoi, lophoc):
        super().__init__(ten, tuoi)
        self.lophoc = lophoc

    def doiLopHoc(self, lopMoi):
        self.lophoc = lopMoi


class GiaoVien(ConNguoi):
    def __init__(self, ten, tuoi):
        
        super().__init(ten, tuoi)


