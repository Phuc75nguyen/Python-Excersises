
def sum_number(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum_number(n[1:])
    
n = [1,2,3,4] 
resuult = sum_number(n)


print("tổng dãy số là:", resuult)