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

for i in range(0, len(dsHocSinh)):
    print(dsHocSinh[i].ten)
    print(dsHocSinh[i].tuoi)
    print(dsHocSinh[i].lopHoc)
    print("Hết một học sinh")

