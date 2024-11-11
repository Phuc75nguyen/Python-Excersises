import math

# Sàng Eratosthenes để tìm các số nguyên tố
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Đếm các số có đúng 9 ước số
def count_numbers_with_9_divisors(N):
    limit = int(math.sqrt(N))
    primes = sieve(limit)
    count = 0
    
    # Kiểm tra các số dạng p^8
    for p in primes:
        if p**8 <= N:
            count += 1
        else:
            break

    # Kiểm tra các số dạng p * q
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] * primes[j] <= N:
                count += 1
            else:
                break

    return count

# Đọc đầu vào
N = int(input())
# Tính và in kết quả
print(count_numbers_with_9_divisors(N))