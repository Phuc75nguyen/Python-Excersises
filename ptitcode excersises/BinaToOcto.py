def binary_to_octal(binary_str):
    # Bổ sung các chữ số 0 vào cụm cuối nếu thiếu
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str

    # Chia số nhị phân thành các cụm 3 chữ số
    result = []
    for i in range(0, len(binary_str), 3):
        # Lấy từng cụm 3 chữ số và chuyển sang hệ cơ số 10
        binary_segment = binary_str[i:i+3]
        decimal_value = int(binary_segment, 2)  # Chuyển cụm nhị phân sang thập phân
        result.append(str(decimal_value))  # Thêm giá trị vào kết quả

    return ''.join(result)

# Nhập vào chuỗi nhị phân
binary_str = input()

# Gọi hàm chuyển đổi và in kết quả
print(binary_to_octal(binary_str))
