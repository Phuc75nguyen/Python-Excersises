"""Viết hàm Python in ra n hàng đầu tiên của tam giác Pascal."""
def pascal_triangle(n):
    """
    In ra n hàng đầu tiên của Tam giác Pascal.
    
    Parameters:
    n (int): Số hàng của tam giác Pascal cần in
    
    Returns:
    List[List[int]]: Danh sách chứa các hàng của Tam giác Pascal
    """
    triangle = []  # Danh sách lưu Tam giác Pascal
    
    for i in range(n):
        # Mỗi hàng mới bắt đầu với giá trị [1]
        row = [1]
        
        if triangle:  # Nếu không phải hàng đầu tiên
            # Lấy hàng trước đó
            prev_row = triangle[-1]
            
            # Tạo hàng mới bằng cách cộng hai số liền kề của hàng trước
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            
            # Kết thúc hàng bằng 1
            row.append(1)
        
        # Thêm hàng mới vào Tam giác Pascal
        triangle.append(row)
    
    return triangle

# Hàm hiển thị Tam giác Pascal
def print_pascal_triangle(triangle):
    """
    Hiển thị Tam giác Pascal dưới dạng đẹp mắt.
    
    Parameters:
    triangle (List[List[int]]): Tam giác Pascal đã tính
    """
    max_width = len(' '.join(map(str, triangle[-1])))  # Tính độ rộng của hàng lớn nhất
    
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))
