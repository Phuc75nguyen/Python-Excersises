"""
Trên cổng thực hành trực tuyến của Học viện Công nghệ Bưu chính 
Viễn thông có danh sách sinh viên trong lớp được xếp hạng để đánh giá kết quả.
Mỗi sinh viên có họ tên, số bài làm đúng, tổng số lượt submit. 
Hãy sắp xếp danh sách sinh viên để có bảng xếp hạng môn học

Thứ tự sắp xếp như sau:

Sinh viên có số bài làm đúng nhiều hơn xếp trước, 
nếu có cùng số bài làm đúng thì ưu tiên sinh viên có số lượt submit ít hơn.
Sinh viên có cùng hạng, xếp họ tên ưu tiên theo thứ tự từ điển lên trước.
"""

# Hàm xử lý việc đọc dữ liệu và sắp xếp danh sách sinh viên
def rank_ptitStudents(N, ds_sinh_vien):
    # Sắp xếp dựa trên số bài làm đúng, số lượt submit và tên
    ds_sinh_vien.sort(key=lambda x: (-x[1], x[2], x[0]))
    
    # In danh sách sinh viên đã sắp xếp
    for sv in ds_sinh_vien:
        print(f"{sv[0]} {sv[1]} {sv[2]}")

# Đọc dữ liệu đầu vào
N = int(input())  # Số lượng sinh viên
ds_sinh_vien = []

for i in range(N):
    ho_ten = input().strip()  # Đọc tên sinh viên
    so_bai_dung, sp_luong_submit = map(int, input().split())  # Đọc số bài làm đúng (so_bai_dung) và số lượt submit (so_luong_submit)
    ds_sinh_vien.append((ho_ten, so_bai_dung, sp_luong_submit))  # Lưu thông tin sinh viên vào danh sách

# Gọi hàm xử lý để sắp xếp và in ra kết quả
rank_ptitStudents(N, ds_sinh_vien)
