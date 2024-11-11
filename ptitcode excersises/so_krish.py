"""
Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các 
chữ số của N bằng chính nó. Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. 
Cho số nguyên dương N, hãy kiểm 
tra N có phải là một số Krish hay không?
Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.

"""


def giaithua(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
def solve(n):
    tong=0
    for i in str(n):
        tong+=giaithua(int(i))
    return n==tong
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print('Yes') if solve(num) else print('No')