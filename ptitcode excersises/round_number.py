def round_number(N):
    factor = 10
    while N > factor:
        remainder = N % factor
        N -= remainder
        if remainder >= factor // 2:
            N += factor
        factor *= 10
    return N

# Input số bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    N = int(input())
    print(round_number(N))
