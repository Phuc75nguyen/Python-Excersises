def upDownNumber(num):
    numStr = str(num)
    if len(numStr) < 3:
        return False
    max_val = -10 ** 18
    for i in numStr:
        max_val = max(max_val, int(i))
    idx_max = numStr.index(str(max_val))

    dayTang=int(numStr[:idx_max+1])
    dayGiam=int(numStr[idx_max:])

    while dayTang>=10:
        r=dayTang%10
        if r<=(dayTang//10)%10:
            return False
        dayTang//=10

    while dayGiam>=10:
        r=dayGiam%10
        if r>=(dayGiam//10)%10:
            return False
        dayGiam//=10

    return True

amountTest = int(input())
for _ in range(amountTest):
    num = int(input())
    print('YES') if upDownNumber(num) else print('NO')