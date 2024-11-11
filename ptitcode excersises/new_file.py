import os
import shutil

# Đường dẫn gốc
root_path = "D:"
# Tạo thư mục 'phuc'
phuc_path = os.path.join(root_path, "phuc")
os.mkdir(phuc_path)

# Tạo các thư mục và tệp tin trong đường dẫn gốc
thuc_hanh_path = os.path.join(root_path, "thuc_hanh")
lythuyet_path = os.path.join(root_path, "lythuyet")
diem_file = os.path.join(root_path, "diem.json")

# Tạo các thư mục 'thuc_hanh' và 'lythuyet'
os.mkdir(thuc_hanh_path)
os.mkdir(lythuyet_path)

# Tạo các tệp tin trong 'thuc_hanh'
open(os.path.join(thuc_hanh_path, "bai_01.py"), "w").close()
open(os.path.join(thuc_hanh_path, "taptin.txt"), "w").close()
open(os.path.join(thuc_hanh_path, "code.c"), "w").close()

# Tạo các tệp tin trong 'lythuyet'
open(os.path.join(lythuyet_path, "chap01.txt"), "w").close()
open(os.path.join(lythuyet_path, "final.txt"), "w").close()

# Tạo tệp 'diem.json' trong thư mục gốc
open(diem_file, "w").close()

# Di chuyển thư mục 'thuc_hanh' vào thư mục 'phuc'
shutil.move(thuc_hanh_path, phuc_path)

# Di chuyển thư mục 'lythuyet' vào thư mục 'phuc'
shutil.move(lythuyet_path, phuc_path)

# Di chuyển tệp 'diem.json' vào thư mục 'phuc'
shutil.move(diem_file, phuc_path)

print("Các thư mục và tệp tin đã được di chuyển vào thư mục 'phuc' thành công.")
