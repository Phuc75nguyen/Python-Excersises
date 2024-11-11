def power(a,b):
    #trường hợp b = 0 thì kết quả trả về là 1
    if b == 0:
        return 1
    #trường hợp số mũ b âm
    elif b < 0:
        return 1/power(a,-b)
    else:
        return a * power(a, b-1)
    
a = float(input())
b = float(input())

ketqua = power(a,b)


print("A mũ B là:", ketqua)