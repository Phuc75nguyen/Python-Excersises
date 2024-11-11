"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa.
 Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và
   viết số lượng phía sau các chữ cái đó.

Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1

Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.

Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng."""

def giaiMaSauKiTu(maHoaSau):
    giai_ma = ""
    i = 0
    while i < len(maHoaSau):
        ki_tu = maHoaSau[i]

        dem = int(maHoaSau[i + 1])


        giai_ma += ki_tu*dem

        i += 2
    return giai_ma


#test case
T = int(input())



for _ in range(T):
    maHoaSau = input()
    print(giaiMaSauKiTu(maHoaSau))