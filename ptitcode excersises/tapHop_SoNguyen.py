# Đọc dữ liệu đầu vào
n, m = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

# Tạo tập hợp từ danh sách a và b để loại bỏ phần tử trùng lặp
set_a = set(a)
set_b = set(b)

# Tính các phép toán trên tập hợp
intersection = sorted(set_a & set_b)  # Giao của A và B
a_minus_b = sorted(set_a - set_b)     # Hiệu của A - B
b_minus_a = sorted(set_b - set_a)     # Hiệu của B - A

# In kết quả
print(" ".join(map(str, intersection)))
print(" ".join(map(str, a_minus_b)))
print(" ".join(map(str, b_minus_a)))
