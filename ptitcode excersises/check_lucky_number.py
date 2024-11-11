"""
Chữ số 4 và chữ số 7được xem là các chữ số may mắn.
Cho số nguyên dương N có không quá 18 chữ số.
Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.
Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
"""

"""
Hướng giải quyết;
str(N): Chuyển số N thành chuỗi để có thể duyệt từng chữ số.
Duyệt từng chữ số: Vòng lặp for duyệt qua từng chữ số trong chuỗi N.
Đếm chữ số 4 và 7: Mỗi khi gặp chữ số 4 hoặc 7, biến count sẽ tăng thêm 1.
Kiểm tra điều kiện: Sau khi đếm xong, kiểm tra xem tổng số lần xuất hiện của 
các chữ số may mắn có bằng 4 hoặc 7 không. Nếu có, in ra "YES", ngược lại in "NO".
"""

def is_lucky_number(N):
    count = 0
    for digit in str(N):
        if digit == '4' or digit == '7':
            count += 1

    if count == 4 or count == 7:
        return "YES"
    else:
        return "NO"

N = int(input())

print(is_lucky_number(N))