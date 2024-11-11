# Dãy ký tự chuẩn
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def ma_hoa(K, S):
    result = []
    for ch in S:
        # Tìm vị trí của ký tự trong P
        idx = P.index(ch)
        # Tính toán ký tự mã hóa
        new_idx = (idx + K) % 28
        result.append(P[new_idx])
    # Đảo ngược chuỗi kết quả
    return ''.join(result[::-1])

# Xử lý input
while True:
    data = input().strip().split()
    K = int(data[0])
    
    if K == 0:
        break
    
    S = data[1]
    print(ma_hoa(K, S))
