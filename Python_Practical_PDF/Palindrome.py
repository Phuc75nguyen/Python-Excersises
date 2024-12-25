"""Chuỗi Palindrome
Viết một hàm Python để kiểm tra xem một chuỗi đã truyền có phải là palindrome hay 
không.
Lưu ý: Palindrome là một từ, cụm từ hoặc trình tự đọc ngược cũng như đọc xuôi, ví dụ: 
madam"""

def is_palindrome(s):
    # bỏ khoảng trắng và chuyển về chữ thường
    s = ''.join(s.split()).lower()
    # So sánh chuỗi với chuỗi đảo ngược của nó
    return s == s[::-1]

# Kiểm tra hàm
"""def main():
    test_string = "madam"
    if is_palindrome(test_string):
        print(f"'{test_string}' là một palindrome.")
    else:
        print(f"'{test_string}' không phải là một palindrome.")"""


if __name__ == "__main__":
    print(is_palindrome("madam")) 
    print(is_palindrome("hello"))          # False
    print(is_palindrome("A Santa at NASA")) # True
    print(is_palindrome("Racecar"))        # True
    print(is_palindrome("Python"))         # False
    