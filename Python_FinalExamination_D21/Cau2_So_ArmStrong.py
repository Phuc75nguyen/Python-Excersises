"""Số amrstrong là số mà từng số trong đó lũy thừa với số chữ số của của nó đúng bằng chính nó
Ví dụ: 153 = 1^1 + 5^5 + 3^3 = 153
a. Viết hàm is_armstrong(n) để kiểm tra n có phải là số armstrong hay không?
b. Viết hàm list_n_armstrong(n) để trả về danh sách n số armstrong đầu tiên.
c. Cho danh sách một dãy số bất kỳ my_list, hãy viết hàm get_armstrong(my_list) để trả về danh sách các số là
số armstrong được sắp xếp theo thứ tự từ bé đến lớn và không được trùng nhau.
d. Cho 1 tập tin chứa văn bản my_text_1.txt. Hãy viết hàm get_frequency(path_to_file), hàm trả về 1 từ điển
với key là số armstrong, value là số lần xuất hiện của key tương ứng trong văn bản, đồng thời lưu lại văn bản vào tập tin
D:\get_frequency.log   
e. Viết hàm min để kiểm thử câu a b c d

"""
import re
#a. Hàm is_armstorn
def is_armstrong(n):
    #chuyển số n thành chuỗi để lặp qua các phần tử
    numbers_string = str(n)
    #tính số chữ số
    num_digits = len(numbers_string)
    #tính tổng lũy thừa
    total = sum(int(digit) ** num_digits for digit in numbers_string)
    #so sánh tổng total với số ban đầu
    return total == n


#b. hàm list_n_armstrong(n) để trả về danh sách n số armstrong đầu tiên
def list_n_armstrong(n):
    #khởi tạo danh sách trống để chứa các số amrstrong vào biến armstrong_nums
    armstong_nums = []
    # biến current đại diện cho số đang được kiểm tra, bắt đầu từ 0
    current = 0
    while len(armstong_nums) < n:
        if(is_armstrong(current)):
            armstong_nums.append 
            # nếu không thì tăng curent lên 1 và tiếp tục kiểm tra
        current += 1
    return armstong_nums



#viết hàm get_armstrong(my_list) để trả về danh sách các số là
#số armstrong được sắp xếp theo thứ tự từ bé đến lớn và không được trùng nhau
def get_armstrong(my_list):
    armstrong_set = {num for num in my_list if is_armstrong(num)}
    return sorted(armstrong_set)

#hàm get_frequency(path_to_file), hàm trả về 1 từ điển
#với key là số armstrong, value là số lần xuất hiện của key tương ứng trong văn bản, 
#đồng thời lưu lại văn bản vào tập tin
def get_frequency(path_to_file):
    try:
        with open(path_to_file, 'r') as file:
            content = file.read()
            
    #Tim tat ca ca so co trong file van ban
        numbers = map(int, re.findall(r'\d+', content))
    
    
    #dem tan suat xuat hien cac so armstrong co trong file van ban
        frequency = {}
        for number in numbers:
            if is_armstrong(number):
                 frequency [number] = frequency.get(number, 0) + 1
    #ghi log vao tep
        with open (r"D:\get_frequency.log", 'w') as log_file:
            log_file.write(f"Frequency of Armstrong numbers:\n {frequency}")
        return frequency

    except  FileNotFoundError:
        print("File not found! Check it again!")
        return{}
    
    
    #e. Ham main de kiem tra thu a b c d
def main():
    # a. Kiểm tra số Armstrong
    print("153 là số Armstrong:", is_armstrong(153))
    print("123 là số Armstrong:", is_armstrong(123))
    
    # b. Danh sách n số Armstrong đầu tiên
    print("5 số Armstrong đầu tiên:", list_n_armstrong(5))

    # c. Danh sách số Armstrong từ dãy cho trước
    my_list = [0, 153, 9474, 371, 9474, 123, 407]
    print("Danh sách Armstrong không trùng lặp:", get_armstrong(my_list))

    # d. Đếm tần suất số Armstrong trong tệp
    path_to_file = "my_text_1.txt"
    print("Tần suất số Armstrong trong file:", get_frequency(path_to_file))


if __name__ == "__main__":
    main()