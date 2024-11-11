def danh_so_ngoac(bieu_thuc):
    stack = []  # Ngăn xếp lưu vị trí dấu ngoặc mở
    result = []  # Danh sách kết quả lưu thứ tự của các dấu ngoặc
    idx = 1  # Chỉ số cho các cặp ngoặc
    
    # Chuyển biểu thức thành danh sách để dễ đánh số
    bieu_thuc = list(bieu_thuc)
    
    # Kết quả sau khi xử lý dấu ngoặc sẽ nằm trong list 'ngoac_ket_qua'
    ngoac_ket_qua = [0] * len(bieu_thuc)
    
    for i in range(len(bieu_thuc)):
        if bieu_thuc[i] == '(':
            stack.append(i)  # Đẩy vị trí ngoặc mở vào stack
            ngoac_ket_qua[i] = idx  # Đánh số cho dấu ngoặc mở
            idx += 1
        elif bieu_thuc[i] == ')':
            vi_tri_mo = stack.pop()  # Lấy vị trí ngoặc mở tương ứng
            ngoac_ket_qua[i] = ngoac_ket_qua[vi_tri_mo]  # Đánh số cho dấu ngoặc đóng
    
    # Chỉ in những số liên quan đến dấu ngoặc
    return ' '.join(str(ngoac_ket_qua[i]) for i in range(len(bieu_thuc)) if ngoac_ket_qua[i] != 0)

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    bieu_thuc = input().strip()
    print(danh_so_ngoac(bieu_thuc))
