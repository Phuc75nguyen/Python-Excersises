def convert_the_base(n, b):
    ans = ''
    temp = n
    while temp > 0:
        r=temp%b
        if r>=10:
            ans+=str(chr(r+55))
        else:
            ans+=str(r)
        temp//=b
    print(''.join(reversed(ans)))


if __name__=='__main__':
    test=int(input())
    for _ in range(test):
        n,b=map(int,input().split())
        convert_the_base(n,b)