import heapq

# Tạo dãy số Hamming bằng cách dùng hàng đợi ưu tiên
def sinh_day_hamming(gioi_han):
    hamming_numbers = []
    pq = []
    heapq.heappush(pq, 1)
    visited = set([1])
    
    while pq:
        current = heapq.heappop(pq)
        hamming_numbers.append(current)
        
        # Dừng lại nếu giá trị vượt qua giới hạn
        if current > gioi_han:
            break
        
        for factor in [2, 3, 5]:
            new_num = current * factor
            if new_num not in visited:
                visited.add(new_num)
                heapq.heappush(pq, new_num)
                
    return hamming_numbers

# Kiểm tra N có phải là số Hamming không
def la_so_hamming(N):
    while N % 2 == 0:
        N //= 2
    while N % 3 == 0:
        N //= 3
    while N % 5 == 0:
        N //= 5
    return N == 1

# Xử lý input
def main():
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]
    
    gioi_han = max(test_cases)
    hamming_numbers = sinh_day_hamming(gioi_han)
    
    # Lưu vào từ điển để truy vấn nhanh
    hamming_dict = {num: i+1 for i, num in enumerate(hamming_numbers)}
    
    for N in test_cases:
        if N in hamming_dict:
            print(hamming_dict[N])
        else:
            print("Not in sequence")

if __name__ == "__main__":
    main()
