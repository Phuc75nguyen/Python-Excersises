#Câu 1, tính tiền taxi
"""stt	kilomet (km)	đơn giá (VND/km)
1	0 đến 0.3	20000
2	 0 đến 3	18600
3	3 đến 11	14200
4	11 đến 20	13000
5	21 đến 30	12000
6	30 trở đi	11000
Nếu đi trên 120km sẽ được giảm 10% trên tổng tiền;
Thuế giá trị gia tăng là 5% trên tổng hóa đơn
Số tiền trả về được làm tròn đến hàng đơn vị

a. Viết hàm taxi_bill_perKm để tính và trả về số tiền đi taxi tương ứng với số km cho trước.
b. Viết chương trình nhập vào chỉ số km, sau đó in ra số tiền phải chi trả.
"""


import math
def taxi_bill_perKm(kilometers):
    # tính giá tiền taxi theo số km 
    if kilometers <= 0.3:
        gia_tien = kilometers*20000
    elif kilometers <= 3:
        gia_tien = kilometers * 18600
    elif kilometers <= 11:
        gia_tien = 3 * 18600 + (kilometers-3)*14200
    elif kilometers <= 20:
        gia_tien = 3* 18600 + 8*14200 + (kilometers-11)*13000
    elif kilometers <= 30:
        gia_tien = 3* 18600 + 8*14200 + 9*13000 + (kilometers-20)*12000
    else:
        gia_tien = (3* 18600 + 8*14200 + 9*1300+ 10*12000 + (kilometers-30)*11000)
        
    #giảm giá 10% nếu đi trên 120km
    if kilometers > 120:
        gia_tien *= 0.9
        
    # thuế giá trị gia tăng 5%
    tong_bill = gia_tien * 1.05


     # Làm tròn số tiền đến hàng đơn vị
    return math.ceil(tong_bill)

           
def main ():
        try:
            kilometers = float(input("Nhập số km đã đi: "))
            if kilometers < 0:
                print("Km phải lớn hơn 0 chứ! Nhập lại đi!")
            else:
                tong_bill = taxi_bill_perKm(kilometers)
                print(f"Số tiền phải trả cho lần đi taxi này là: {tong_bill} VND")
        except ValueError:
            print("Vui lòng nhập số km hợp lệ!")

if __name__ == "__main__":
      #a. kiểm tra các trường hợp bằng số km cho trước
    print("Các trường hợp km theo bảng giá!")
    print("0 đến 0.3km:",taxi_bill_perKm(0.25), "VND")
    print("0.3 đến 3km:",taxi_bill_perKm(2), "VND")
    print("3 đến 11km:",taxi_bill_perKm(9), "VND")
    print("11 đến 20km :",taxi_bill_perKm(19), "VND")
    print("21 đến 30km:",taxi_bill_perKm(25), "VND")
    print("30km trở đi:",taxi_bill_perKm(50), "VND")
    print("Trên 120 km :",taxi_bill_perKm(260), "VND")

    #b. chương trình nhập vào chỉ số km, sau đó in ra số tiền phải chi trả.
    main()
    

  