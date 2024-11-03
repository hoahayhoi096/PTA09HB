from classes.HocSinh import HocSinh

hocSinh1 = HocSinh("Kiên", 13, "PTA09")
hocSinh2 = HocSinh("Khang", 12, "PTA09")
hocSinh3 = HocSinh("Thiện", 13, "PTA09")

lop_pta09 = [hocSinh1, hocSinh2, hocSinh3]


print(hocSinh1.ten)

hocSinh1.doiTen("Quân")

print("Tên mới: ", hocSinh1.ten)

print("Tuổi cũ", hocSinh1.tuoi)

hocSinh1.capNhatTuoi(14)

print("Tuổi mới: ", hocSinh1.tuoi)


