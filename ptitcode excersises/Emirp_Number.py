"""
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố,
đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). 
Ví dụ số 11 không phải là số Emirp Number. 
Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.



Ý tưởng giải quyết:
Tìm số nguyên tố: Đầu tiên, ta cần tìm tất cả các số nguyên tố nhỏ hơn 
N. Đây có thể được thực hiện bằng thuật toán Sàng Eratosthenes.

Kiểm tra số đảo ngược: Đối với mỗi số nguyên tố p
p nhỏ hơn N
N, ta cần kiểm tra xem số đảo ngược của nó có phải là một số nguyên tố hay không.
Nếu số đảo ngược khác chính nó và là số nguyên tố, thì p là một số Emirp.

Sắp xếp và in kết quả: In ra các số Emirp theo thứ tự từ nhỏ đến lớn cho mỗi bộ test.
"""


import math

# Hàm sàng Eratosthenes để tìm tất cả các số nguyên tố nhỏ hơn n
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

# Hàm đảo ngược số
def reverse_number(n):
    return int(str(n)[::-1])

# Hàm kiểm tra Emirp
def find_emirp_numbers(n):
    # Tìm các số nguyên tố nhỏ hơn n
    is_prime = sieve_of_eratosthenes(n)
    emirp_numbers = []
    
    for i in range(2, n):
        if is_prime[i]:
            reversed_i = reverse_number(i)
            # Kiểm tra xem số đảo ngược có phải là số nguyên tố và khác với chính nó không
            if reversed_i != i and reversed_i < n and is_prime[reversed_i]:
                emirp_numbers.append(i)
    
    return emirp_numbers

# Xử lý nhiều bộ test
def process_tests(test_cases):
    results = []
    for n in test_cases:
        emirp_numbers = find_emirp_numbers(n)
        results.append(' '.join(map(str, emirp_numbers)))
    return results

# Đọc input và xử lý
T = int(input())  # Số lượng bộ test
test_cases = [int(input()) for _ in range(T)]

# Tìm và in kết quả cho mỗi bộ test
results = process_tests(test_cases)
for result in results:
    print(result)
