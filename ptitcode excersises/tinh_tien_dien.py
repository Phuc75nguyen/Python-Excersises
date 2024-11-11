"""
Các hộ gia đình trong thành phố X được chia thành 3 loại A, B, C với định mức sử dụng điện như sau:

Loại A: Định mức 100 kWh
Loại B: Định mức 500 kWh
Loại C: Định mức 200 kWh
Hãy tính toán số tiền phải thanh toán theo quy tắc:

Tính tiền trong định mức:

Nếu số điện (Số cuối - Số đầu) nhỏ hơn định mức thì bằng số điện * 450                 

Nếu số điện lớn hơn hoặc bằng định mức thì bằng định mức *450                                             

Tiền vượt định mức                                                                                  

Nếu số điện lớn hơn định mức thì bằng (số điện - định mức) *1000                                      

Ngược lại thì bằng 0

Thuế VAT = 5% số tiền vượt định mức.

Chú ý: tiền thuế VAT cũng là số nguyên dương nên có thể lấy 
số tiền vượt định mức chia phần nguyên cho 20.

 

Số tiền phải nộp = Tiền trong định mức + Tiền vượt định mức + Thuế VAT

 

Input

Dòng đầu ghi số khách hàng (không quá 50).

Mỗi khách hàng ghi trên 2 dòng:

Họ tên: có thể chưa chuẩn hóa
Loại hộ gia đình, chỉ số đầu, chỉ số cuối. Mỗi thông tin cách nhau một khoảng trống.
Output

Ghi ra danh sách đã sắp xếp theo tổng số tiền phải trả giảm dần gồm các thông tin:

Mã khách hàng: tính từ KH01 theo thứ tự nhập
Họ tên đã chuẩn hóa
Tiền trong định mức
Tiền vượt định mức
Thuế VAT
Tổng số tiền phải nộp.
"""

#Ham chuan hoa ho ten
# Hàm chuẩn hóa họ và tên
def chuan_hoa_HovaTen(hoTen):
    return ' '.join(word.capitalize() for word in hoTen.strip().split())

# Hàm tính tiền điện
def tinh_tien_dien(dien, dinh_muc):
    if dien < dinh_muc:
        tien_trong_muc = dien * 450
        tien_vuot_muc = 0  # Gán giá trị tiền vượt mức là 0 nếu số điện nhỏ hơn định mức
    else:
        tien_trong_muc = dinh_muc * 450
        tien_vuot_muc = (dien - dinh_muc) * 1000
    
    thue_VAT = tien_vuot_muc // 20  # Tính thuế VAT
    tong_tien = tien_trong_muc + tien_vuot_muc + thue_VAT  # Tính tổng tiền phải nộp
    return tien_trong_muc, tien_vuot_muc, thue_VAT, tong_tien

# Đọc số lượng khách hàng
T = int(input())

ho_GD = []  # Danh sách các hộ gia đình
dinh_muc = {'A': 100, 'B': 500, 'C': 200}  # Định mức điện cho từng loại hộ gia đình

# Xử lý từng khách hàng
for i in range(T):
    # Đọc họ tên và loại hộ gia đình, chỉ số điện
    ho_ten = input().strip()
    loai_ho, chi_so_dau, chi_so_cuoi = input().split()

    # Tính số điện tiêu thụ
    chi_so_dau = int(chi_so_dau)
    chi_so_cuoi = int(chi_so_cuoi)
    
    so_dien_tieu_thu = chi_so_cuoi - chi_so_dau

    # Chuẩn hóa họ tên
    ho_ten_chuanhoa = chuan_hoa_HovaTen(ho_ten)

    # Tính tiền điện
    dinh_muc_ho = dinh_muc[loai_ho]
    tien_trong_muc, tien_vuot_muc, thue_VAT, tong_tien = tinh_tien_dien(so_dien_tieu_thu, dinh_muc_ho)

    # Lưu lại thông tin hộ gia đình
    ho_GD.append((f"KH{i+1:02d}", ho_ten_chuanhoa, tien_trong_muc, tien_vuot_muc, thue_VAT, tong_tien))

# Sắp xếp danh sách hộ gia đình theo tổng số tiền phải trả giảm dần
ho_GD.sort(key=lambda x: x[5], reverse=True)

# In kết quả
for hogd in ho_GD:
    print(f"{hogd[0]} {hogd[1]} {hogd[2]} {hogd[3]} {hogd[4]} {hogd[5]}")
