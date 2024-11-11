class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

    # Phương thức nhập ma trận
    def input_matrix(self):
        for _ in range(self.rows):
            row = list(map(int, input().split()))
            self.data.append(row)

    # Phương thức tính ma trận chuyển vị
    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        transposed_matrix = Matrix(self.cols, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    # Phương thức nhân ma trận hiện tại với ma trận khác
    def multiply(self, other):
        result = Matrix(self.rows, other.cols)
        result.data = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    # Phương thức hiển thị ma trận
    def display(self):
        for row in self.data:
            print(" ".join(map(str, row)))

# Đọc số bộ test
t = int(input())
for _ in range(t):
    # Đọc kích thước ma trận
    n, m = map(int, input().split())
    # Khởi tạo và nhập ma trận
    matrix_a = Matrix(n, m)
    matrix_a.input_matrix()
    # Tính ma trận chuyển vị
    matrix_at = matrix_a.transpose()
    # Tính tích của a và a chuyển vị
    result_matrix = matrix_a.multiply(matrix_at)
    # Hiển thị kết quả
    result_matrix.display()
