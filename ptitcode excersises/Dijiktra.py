import heapq

def dijkstra(N, M, A):
    # Ma trận chi phí ban đầu, khởi tạo với giá trị vô cùng lớn
    dist = [[float('inf')] * M for _ in range(N)]
    dist[0][0] = 0  # Vị trí bắt đầu có chi phí là 0
    
    # Hàng đợi ưu tiên để thực hiện Dijkstra
    pq = [(0, 0, 0)]  # (cost, x, y)
    
    directions = [(1, 0), (0, 1), (1, 1)]  # Các hướng: xuống, phải, chéo
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        
        if x == N-1 and y == M-1:  # Đến đích
            return cost
        
        # Thử 3 hướng di chuyển
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # Tính chi phí di chuyển
                if dx == 1 and dy == 0:  # Di chuyển xuống dưới
                    move_cost = abs(A[x][y] - A[nx][ny])
                elif dx == 0 and dy == 1:  # Di chuyển sang phải
                    move_cost = abs(A[x][y] - A[nx][ny])
                else:  # Di chuyển chéo xuống
                    move_cost = abs(A[x][y] - A[nx][ny])
                
                # Nếu tìm được con đường ngắn hơn
                if cost + move_cost < dist[nx][ny]:
                    dist[nx][ny] = cost + move_cost
                    heapq.heappush(pq, (dist[nx][ny], nx, ny))
    
    # Nếu không thể đến đích
    return -1

def solve():
    T = int(input())  # Đọc số lượng test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Kích thước ma trận
        A = [list(map(int, input().split())) for _ in range(N)]  # Đọc ma trận A
        
        # Tính toán số bước đi ít nhất
        result = dijkstra(N, M, A)
        
        print(result)

# Chạy hàm solve để nhận kết quả
solve()
