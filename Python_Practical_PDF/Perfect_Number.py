"""Số hoàn hảo
Viết hàm Python để kiểm tra xem một số có hoàn hảo hay không.
Theo Wikipedia: Trong lý thuyết số, một số hoàn hảo là một số nguyên dương bằng tổng 
các ước số dương thực sự của nó, nghĩa là tổng các ước số dương của nó không bao gồm 
chính số đó (còn được gọi là tổng các phần tử của nó). Tương tự, một số hoàn hảo là một 
số bằng một nửa tổng của tất cả các ước dương của nó (bao gồm cả chính nó).
"""


#hàm kiểm tra có phải là một số hoàn hảo
def is_perfect_number(n):
    if n < 0:
        return False
    tong_uoc = sum(i for i in range(1, n) if n % i == 0)
    return tong_uoc == n

def count_perfect(str_input):
    words = str_input.split()
    count = 0
    for word in words:
        if word.isdigit() and is_perfect_number(int(word)):
            count += 1
    return count

def count_unique_perfect(str_input):
    words = str_input.split()
    unique_perfects = set()
    for word in words:
        if word.isdigit() and is_perfect_number(int(word)):
            unique_perfects.add(int(word))
    return len(unique_perfects)

def max_frequent_perfect(str_input):
    from collections import Counter
    
    words = str_input.split()
    perfect_counts = Counter()
    for word in words:
        if word.isdigit() and is_perfect_number(int(word)):
            perfect_counts[int(word)] += 1

    if not perfect_counts:
        return None
    return max(perfect_counts, key=perfect_counts.get)

# Test các hàm
str_input = "6 28 6 496 8128 28 8128 10 12"
print("Số lượng số hoàn hảo:", count_perfect(str_input))  # Kết quả: 8
print("Số lượng số hoàn hảo không trùng nhau:", count_unique_perfect(str_input))  # Kết quả: 4
print("Số hoàn hảo xuất hiện nhiều nhất:", max_frequent_perfect(str_input))  # Kết quả: 6