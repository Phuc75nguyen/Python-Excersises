"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ ‘a’, ‘b’, …, ‘z’ và các số từ 0 đến 9. Nhiệm vụ của bạn là tìm số lớn nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 29.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
Output:

Đưa ra kết quả mỗi test theo từng dòng.

"""

import re

def Find_Max_Number(s):
    #tiep tuc sd regrex để tìm chuỗi số trong xâu liên tiếp
    number_in_string = re.findall(r'\d+',s)
    #chuyển chuỗi số về số nguyên
    number_in_string = [int (x) for x in number_in_string]
    #trả về số lớn nhất
    return max(number_in_string)

#đọc số lượng test T
T = int(input())

#xử lý bộ test
for _ in range(T):
    s = input().strip()
    print(Find_Max_Number(s))
