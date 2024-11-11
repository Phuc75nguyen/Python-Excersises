
"""
Cho dữ liệu vào là luồng văn bản bất kỳ, gồm các ký tự viết hoa, 
viết thường, các ký tự số và các dấu câu, không có các ký tự đặc biệt khác.
Người ta muốn tách văn bản thành các câu. Mỗi câu in trên một dòng.

Một câu được định nghĩa là dãy ký tự có ít nhất 1 ký tự chữ cái hoặc chữ số, 
không chứa các dấu ngắt câu gồm: dấu chấm (.), dấu chấm hỏi (?) và dấu chấm cảm (!). 
Dấu phẩy (,) và dấu hai chấm (:) không được coi là dấu ngắt câu.

Nhiệm vụ của bạn là in ra mỗi câu trên một dòng,
ký tự đầu câu viết hoa, các ký tự khác viết thường, 
các từ cách nhau đúng một khoảng trống. Không có khoảng trống
ở đầu và cuối câu, và không in ra các dấu ngắt câu.

 

Dữ liệu vào

Gồm một luồng văn bản không quá 100 dòng, mỗi dòng không quá 200 ký tự.

 

Kết quả

In ra các câu, mỗi câu trên một dòng theo quy tắc đã cho.

 
"""


"""import re

res=''
regex='\\.\\!\\?'

while True:
    try: res+=input()
    except EOFError: break
res=re.split(regex,res)

for i in res:
    x=i.lower().split()
    x[0]=x[0].title()
    print(*x)"""
    
import re

def chuan_hoa_cau(cau):
    cau = cau.strip()  # Loại bỏ khoảng trắng thừa ở đầu và cuối
    if len(cau) == 0:
        return ''
    
    cau = cau.lower()  # Chuyển tất cả thành chữ thường
    cau = cau.capitalize()  # Viết hoa ký tự đầu
    cau = ' '.join(cau.split())  # Loại bỏ khoảng trắng thừa giữa các từ
    return cau

def tach_cau_van_ban(van_ban):
    # Sử dụng regex để tách các câu theo dấu chấm, chấm hỏi, chấm than
    cau_list = re.split(r'[.!?]+', van_ban)
    return cau_list

# Đọc input từ nhiều dòng
van_ban = ""
while True:
    try:
        dong = input().strip()
        if dong == "":
            break
        van_ban += " " + dong
    except EOFError:
        break

# Tách câu
cau_list = tach_cau_van_ban(van_ban)

# Chuẩn hóa và in từng câu
for cau in cau_list:
    cau_chuan = chuan_hoa_cau(cau)
    if cau_chuan:
        print(cau_chuan)
