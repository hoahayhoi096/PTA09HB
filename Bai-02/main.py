class HocSinh:
    ten = ""
    tuoi = 0
    lopHoc = ""

hocSinh1 = HocSinh()
hocSinh1.ten = "Bảo"
hocSinh1.tuoi = 12
hocSinh1.lopHoc = "PTA09"

hocSinh2 = HocSinh()
hocSinh2.ten = "Kiên"
hocSinh2.tuoi = 13
hocSinh2.lopHoc = "PTA09"

dsHocSinh = [hocSinh1, hocSinh2]

# In ra màn hình các giá trị của các thuộc tính của học sinh 1 
# print(hocSinh1.ten)
# print(hocSinh1.tuoi)
# print(hocSinh1.lopHoc)

# for i in range(0, len(dsHocSinh)):
#     print(dsHocSinh[i].ten)
#     print(dsHocSinh[i].tuoi)
#     print(dsHocSinh[i].lopHoc)
#     print("Hết một học sinh")


class Xe:
    hangXe = ""
    soChoNgoi = 0 
    mauSac = ""

xe1 = Xe()
xe1.hangXe = "Toyota"
xe1.soChoNgoi = 4 
xe1.mauSac = "Đỏ"

xe2 = Xe()
xe2.hangXe = "Lambogini"
xe2.soChoNgoi = 2 
xe2.mauSac = "Vàng"

dsXe = [xe1, xe2]

for i in range(0, len(dsXe)):
    print(dsXe[i].hangXe)
    print(dsXe[i].soChoNgoi)
    print(dsXe[i].mauSac)
    print("")