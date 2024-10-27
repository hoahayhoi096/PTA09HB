# Biến là gì? Cách sử dụng biến? 

# Danh Sách? Cách sử dụng danh sách?
# ds_1 = [1, 2, 3, 8, 5 , 12, 10]
# ds_1.append(13)
# ds_1.remove(3)
# print(ds_1)
# for i in range(len(ds_1)): 
#     print(ds_1[i])


# Xâu? Cách sử dụng xâu? 
# str = "sdfsdfsdfasdf"
# str2 = "sdf2"

# if ( str2 in str): 
#     print("str2 là con của str")

# Hàm? Cách sử dụng hàm? 
# def hello():
#     print("Xin chào các bạn!")

# hello()

# Hàm không có giá trị trả về 

# Hàm có giá trị trả về
# def tongBaSo(a, b ,c):
#     ketQua = a + b + c
#     return ketQua

# kq = tongBaSo(1, 2, 3)
# print(kq)

# Làm bài tập 

# ban1 = int(input("Nhập chiều cao bạn a: "))
# ban2 = int(input("Nhập chiều cao bạn b: "))
# ban3 = int(input("Nhập chiều cao bạn c: "))

# if ban1 > ban2 and ban1 > ban3:
#     print("Bạn a cao nhất")
# elif ban2 > ban1 and ban2 > ban3: 
#     print("Bạn b cao nhất")
# elif ban3 > ban2 and ban3 > ban1:
#     print("Bạn c cao nhất")
# else :
#     print("Không hợp lệ")


# Nhập ds n các số nguyên 
def nhapDS():
    ds = []
    n = int(input("Nhập số phần tử của danh sách: "))
    for i in range(n):
        number = int(input("Nhập vào phần tử của danh sách: "))
        ds.append(number)
    return ds 

def xoaSoLe(ds):
    # Loại bỏ số chẵn trong danh sách
    for phan_tu in ds[:]:  # Sử dụng danh sách sao chép để tránh lỗi khi thay đổi danh sách
        if phan_tu % 2 == 1:
            ds.remove(phan_tu)

    return ds

ds_1 = nhapDS()

print(ds_1)

ds_2 = xoaSoLe(ds_1)
print(ds_2)