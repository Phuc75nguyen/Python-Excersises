"""
Thẻ căn cước công dân (cccd) gồm 12 chữ số : AAABCCDDDDDD, với AAA là mã tỉnh thành, B là mã giới tính và mã thế kỷ
CC là 2 chữ số cuối cùng của năm sinh, DDDDDD là một dãy số ngẫu nhiên. Thông qua dãy số này, cơ quan quản lý có thể xác định 
một số thông tin của người sở hữu thẻ cccd, giả định rằng số thẻ cccd được xác thực theo các bước sau:
- Bắt đầu từ chữ số ngoài cùng bên phải, nhân đôi giá trị của mỗi chữ số thứ 2
- Nếu nhân đôi 1 số dẫn đến một số có 2 chữ số, tức là lớn hơn 9, sau đó cộng các chữ số của tích, để được một số có 1 chữ số
- Bây giờ lấy tổng của tất cả các chữ số 
-Kiểm tra xe có chia hết cho 10 hay không (tổng modulo cho 10 bằng 0) thì số IMEI hợp lệ, nếu khác là không hợp lệ 
Ví dụ 079203000009 là số cccd hợp lệ vì tinh_tong là 30 modulo cho 10 bằng 0

a. Hãy viết hàm  is_valid_cccd(cccd) để kiểm tra chuỗi số cccd nhập vào có phải là số thẻ cccd hợp lệ.Sau đó viết hàm kiểm thử.
b. Giả định rằng số thẻ cccd bị hư hại và mất một số ở vị trí cuối cùng (ví dụ:07920300000X), hãy viết hàm get_all_cccd(atm), để trả về danh sách 
các số cccd hợp lệ (tức là đoán số cccd)
"""
#a. hàm is_valid_cccd(cccd)

def is_valid_cccd(cccd):
    """Kiểm tra tính hợp lệ của chuỗi chữ số có trong cccd"""
    #đảm bảo chuỗi chỉ chứa số và có đúng 12 kí tự
    if not cccd.isdigit() or len(cccd) != 12:
        return False
    
    total = 0
    for i, char in enumerate(reversed(cccd)):
        digit = int(char)
        #nhân đôi nếu là chữ số thứ 2 từ bên phải
        if i % 2 == 1:
            digit *= 2
            #Nếu kết quả lớn hơn 9, tách ra và cộng các chữ số
            if digit > 9:
                digit = digit // 10 + digit % 10
        total += digit
#Kiểm tra đã hợp lệ chưa
    return total % 10 == 0 


#b. hàm get_all_cccd(atm), để trả về danh sách các số cccd hợp lệ (tức là đoán số cccd)
def get_all_cccd(atm):
    """Trả về danh sách các số CCCD hợp lệ từ số CCCD thiếu chữ số cuối."""
    if not atm[:-1].isdigit() or len(atm) != 12:
        raise ValueError("CCCD phải đủ 12 số. Trong đó X là vị trí bị hư hại, bị thiếu.")
    
    valid_cccd = []
    
    
    for digit in range(10):
        possible_atm = atm[:-1] + str(digit)
        if is_valid_cccd(possible_atm):
            valid_cccd.append(possible_atm)
    return valid_cccd



# Hàm main để kiểm tra thử
if __name__ == "__main__":
    # Kiểm tra CCCD hợp lệ
    test_cccd = "079203000009"
    print(f"Số CCCD {test_cccd} {'hợp lệ' if is_valid_cccd(test_cccd) else 'không hợp lệ'}.")

    # Dự đoán CCCD từ chuỗi thiếu số cuối
    test_cccd_missing = "07920300000X"
    valid_guesses = get_all_cccd(test_cccd_missing)
    print(f"Các số CCCD hợp lệ từ {test_cccd_missing}: {valid_guesses}")
