# Đọc dữ liệu đầu vào
n = int(input().strip())  # Số phần tử trong dãy
arr = list(map(int, input().strip().split()))  # Dãy số A[]

# Khởi tạo giá trị min_steps lớn, lưu lại giá trị tối ưu
min_steps = float('inf')
optimal_value = None

# Duyệt qua từng giá trị trong dãy
for target in arr:
    # Tính tổng số bước để biến tất cả phần tử thành giá trị `target`
    steps = sum(abs(x - target) for x in arr)
    
    # Cập nhật min_steps và optimal_value nếu tìm được số bước ít hơn
    if steps < min_steps:
        min_steps = steps
        optimal_value = target

# In ra tổng số bước ít nhất và giá trị tối ưu
print(min_steps, optimal_value)
