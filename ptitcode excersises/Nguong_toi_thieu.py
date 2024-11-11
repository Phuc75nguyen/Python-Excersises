from collections import Counter

def solve():
    # Đọc dãy ký tự số và ngưỡng tối thiểu K
    s = input().strip()  # Dãy ký tự số
    K = int(input().strip())  # Ngưỡng tối thiểu K
    
    # Tạo danh sách các số 2 chữ số từ dãy số
    A = [int(s[i:i+2]) for i in range(0, len(s) - 1, 2)]
    
    # Đếm số lần xuất hiện của từng số
    count = Counter(A)
    
    # Lọc ra các số có số lần xuất hiện >= K
    result = [(num, freq) for num, freq in count.items() if freq >= K]
    
    if result:
        # Sắp xếp các số theo thứ tự tăng dần và in ra kết quả
        result.sort()
        for num, freq in result:
            print(num, freq)
    else:
        print("NOT FOUND")

# Chạy hàm solve để nhận kết quả
solve()
