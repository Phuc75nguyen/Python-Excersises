def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a==1
def reverse(n):
    rev=0
    while n!=0:
        rev=rev*10+n%10
        n//=10
    return rev

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print('YES') if ucln(num,reverse(num)) else print('NO')