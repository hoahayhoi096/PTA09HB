class Xe: 
    def __init__(self, hang, mau_sac, gia_tien):
        self.hang = hang
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien

    def khoi_dong(self):
        print("Xe", self.hang, "đang khởi động")

class XeDap(Xe):
    def __init__(self, hang, mau_sac, gia_tien):
        super().__init__(hang, mau_sac, gia_tien)
    
    def dap_bang_hai_chan(self):
        print("Xe", self.hang, "đang được đạp về phía trước")

class XeHoi(Xe):
    def __init__(self, hang, mau_sac, gia_tien):
        super().__init__(hang, mau_sac, gia_tien)

    def chay_bang_bon_banh(self):
        print("Xe", self.hang, "đang chạy về phía trước bằng động cơ")

    