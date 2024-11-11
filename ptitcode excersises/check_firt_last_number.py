# Đọc số lượng test cases
T = int(input())

# Lặp qua từng test case
for _ in range(T):
    # Nhập số N
    N = input().strip()
    
    # Lấy 2 chữ số đầu và 2 chữ số cuối
    first_two = N[:2]
    last_two = N[-2:]
    
    # Kiểm tra xem 2 chữ số đầu và cuối có giống nhau không
    if first_two == last_two:
        print("YES")
    else:
        print("NO")
