"""
Nhập xâu ký tự S có độ dài không quá 100. Một từ được định nghĩa là một dãy ký tự không có khoảng trống.  

Hãy tách xâu S thành các từ, mỗi từ in trên một dòng.

"""

#nhập xâu S

S = input().strip()

#tách khoảng trắng

words = S.split()


#in trên 1 dòng
for word in words:
    print(word)