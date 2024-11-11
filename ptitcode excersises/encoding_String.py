def encode_string(s):
    encoded_str = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoded_str += str(count) + s[i]
        i += 1
    return encoded_str

# Đọc số lượng bộ test
T = int(input())

# Duyệt qua từng bộ test
for _ in range(T):
    s = input().strip()  # Đọc vào xâu ký tự
    print(encode_string(s))
