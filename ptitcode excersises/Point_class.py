import math

# Khai báo lớp Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Phương thức tính khoảng cách giữa hai điểm
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Khai báo lớp Triangle
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # Phương thức kiểm tra có tạo thành tam giác không
    def is_valid(self):
        # Tính độ dài ba cạnh
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        # Kiểm tra điều kiện tam giác
        return a + b > c and a + c > b and b + c > a

    # Phương thức tính chu vi tam giác
    def perimeter(self):
        # Tính độ dài ba cạnh
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        # Tính chu vi
        return round(a + b + c, 3)


# Đọc số bộ test
t = int(input())

# Xử lý mỗi bộ test
for _ in range(t):
    # Đọc tọa độ của ba điểm
    x1, y1, x2, y2, x3, y3 = map(float, input().split())

    # Tạo ba đối tượng Point
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)

    # Tạo đối tượng Triangle
    triangle = Triangle(p1, p2, p3)

    # Kiểm tra và in chu vi hoặc thông báo INVALID
    if triangle.is_valid():
        print(triangle.perimeter())
    else:
        print("INVALID")
