def total(n):
    total=0
    for x in str(n):
        total+=int(x)
    return total

def palind(n):
    rev=0
    temp=n
    while n!=0:
        rev=rev*10+n%10
        n//=10
    return rev==temp

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        tong=total(num)
        if palind(tong) and len(str(tong))>=2:
            print('YES')
        else:
            print('NO')