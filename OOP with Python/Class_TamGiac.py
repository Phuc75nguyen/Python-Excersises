"""Xây dựng Lớp hình tam giác với các thuộc tính là chiều dài ba cạnh của tam giác, màu sắc; 
các hàm thành phần gồm tính chu vi, diện tích hình tam giác, hàm hiển thị thông tin hình 
tam giác ra màn hình, hàm hiển thị loại của tam giác như: Tam giác cân, vuông, vuông cân, 
đều, tam giác thường"""
import math

class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c, color):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c
        self.color = color
    
    # Hàm __str__ trả về các thông tin trong tam giác
    def __str__(self):
        return f"Tam giác có màu sắc là {self.color}, có cạnh a là: {self.canh_a}, cạnh b là: {self.canh_b}, cạnh c là: {self.canh_c}"
    
    # Hàm tính chu vi hình tam giác
    def chuViTamGiac(self):
        return self.canh_a + self.canh_b + self.canh_c
    
    # Hàm tính diện tích tam giác
    def dienTichTamGiac(self):
        p = self.chuViTamGiac() / 2  # Tính nửa chu vi
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))
    
    # Hàm kiểm tra loại của tam giác
    def loaiTamGiac(self):
        a, b, c = self.canh_a, self.canh_b, self.canh_c
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"

class quanLyTamGiac:
    def __init__(self):
        # Khởi tạo danh sách tam giác
        self.dsTamGiac = []
    
    # Hàm thêm tam giác vào danh sách
    def themTamGiac(self, tamgiac):
        self.dsTamGiac.append(tamgiac)
    
    # Hàm hiển thị thông tin tam giác ra màn hình
    def hienThiThongTinTamGiac(self):
        print("Thông tin các tam giác:")
        for tamgiac in self.dsTamGiac:
            print(tamgiac)
            print(f"Chu vi: {tamgiac.chuViTamGiac()}")
            print(f"Diện tích: {tamgiac.dienTichTamGiac():.2f}")
            print(f"Loại: {tamgiac.loaiTamGiac()}")
            print("-" * 30)

# Hàm main
if __name__ == "__main__":
    # Tạo các tam giác
    tamgiac1 = TamGiac(3, 4, 5, "Đỏ")
    tamgiac2 = TamGiac(7, 7, 7, "Xanh")
    tamgiac3 = TamGiac(8, 8, 12, "Vàng")
    
    # Thêm vào danh sách
    qlTamGiac = quanLyTamGiac()
    qlTamGiac.themTamGiac(tamgiac1)
    qlTamGiac.themTamGiac(tamgiac2)
    qlTamGiac.themTamGiac(tamgiac3)
    
    # Hiển thị thông tin các tam giác
    qlTamGiac.hienThiThongTinTamGiac()
