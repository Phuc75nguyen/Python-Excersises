# Đọc dữ liệu đầu vào
N, K = map(int, input().strip().split())  # N: số phần tử, K: chênh lệch tối đa
A = list(map(int, input().strip().split()))  # Dãy số A[]

# Nếu dãy rỗng thì không cần nhóm gì cả
if N == 0:
    print(0)
else:
    # Sắp xếp dãy A để dễ dàng tách nhóm
    A.sort()

    # Biến đếm số nhóm
    groups = 1  # Ban đầu có ít nhất một nhóm

    # Duyệt qua các phần tử trong dãy đã sắp xếp
    first = A[0]  # Phần tử đầu tiên trong nhóm hiện tại

    for i in range(1, N):
        # Nếu phần tử hiện tại và phần tử đầu tiên trong nhóm có chênh lệch > K, tạo nhóm mới
        if A[i] - first > K:
            groups += 1
            first = A[i]  # Bắt đầu nhóm mới với phần tử hiện tại

    # In kết quả
    print(groups)
