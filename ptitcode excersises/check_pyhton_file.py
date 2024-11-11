"""
Một file code Python sẽ có phần mở rộng là .py. 

Trong hệ điều hành Windows tên file sẽ không phân biệt chữ hoa, 
chữ thường. Hãy kiểm tra xem tên file có đúng là file code Python hay không. 

Input
Chỉ có một dòng ghi tên file S (1 ≤ |S| ≤ 128). 
Tên file chỉ chứa các ký tự ‘a’-‘z’, ‘A’-‘Z’, ‘.’ và dấu ‘_’.

Output
In ra "yes" hoặc "no" tùy thuộc kết quả kiểm tra.
"""

S = input().strip() # strip() dùng loại bỏ khoảng trắng thừa ở đầu và cuối

#Kiểm tra có phải file ".py"
if S.lower().endswith('.py'):
    print("yes")
else:
    print("no")
 
 
