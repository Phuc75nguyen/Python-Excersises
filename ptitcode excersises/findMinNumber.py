"""

Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9.
 Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
Output:

Đưa ra kết quả mỗi test theo từng dòng.
"""
import re

def Find_Minimum_Number(s):
    # Sử dụng regex để tìm tất cả các chuỗi số liên tiếp
    so_trong_xau = re.findall(r'\d+', s)
    
    # Chuyển tất cả các chuỗi số thành số nguyên
    so_trong_xau = [int(x) for x in so_trong_xau]
    
    # Trả về số nhỏ nhất
    return min(so_trong_xau)

# Đọc vào số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    s = input().strip()
    print(Find_Minimum_Number(s))
