"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. 
Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:

Tổng các chữ số ở vị trí chẵn
Tích các chữ số ở vị trí lẻ. giá trị tích chữ số có thể đến 18 chữ số.
Chú ý khi tính tích bỏ qua các chữ số 0, nhưng nếu tất cả các vị trí lẻ đều là giá trị 0 thì tích = 0.

"""

def sum(n):
    sum = 0
    length = len(str(n))
    for i in range(0,length,2):
        sum += int(str(n)[i])
    return sum
def check(n):
    length = len(str(n))
    for i in range(1,length,2):
        if int(str(n)[i])!=0:
            return False
    return True
def multi(n):
    temp = 1
    length = len(str(n))
    kiem_tra = check(n)
    for i in range(1,length,2):
        if kiem_tra:
            temp = 0
        else:
            if int(str(n)[i]) == 0:
                continue
            temp *= int(str(n)[i])
    return temp

n=int(input())
for _ in range(n):
    num = input()
    print(sum(num),multi(num),sep = ' ')