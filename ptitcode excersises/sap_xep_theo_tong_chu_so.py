""""Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.

Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

Input

Dòng đầu ghi số bộ test (không quá 10)

Mỗi bộ test gồm 2 dòng:

Dòng đầu là số N (N < 100)
Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.
Output

Với mỗi bộ test, ghi trên một dòng dãy số kết quả."""

def total(n):
    total=0
    while n!=0:
        total+=n%10
        n//=10
    return total
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        a.sort(key=total)
        print(*a)
            