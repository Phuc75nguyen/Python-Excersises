def kiemTraIp(ip):
    thanhPhan=ip.split('.') #tách xau và thêm vô dấu .
    if len(thanhPhan)!=4: #kiem tra xem có bằng 4 
        return False
    for con in thanhPhan:
        if not con.isdigit() or not 0<=int(con)<=255: #kiem tra xem có phải là chữ số hoặc 0<con<=255
            return False
    return True

if __name__=='__main__':
    slgTest=int(input())
    for _ in range(slgTest):
        ip=input()
        print('YES') if kiemTraIp(ip) else print('NO')