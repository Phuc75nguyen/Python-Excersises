import os

# Tạo các thư mục
os.mkdir('D:/phuc')
os.mkdir('D:/phuc/thuc hanh')
os.mkdir('D:/phuc/ly thuyet')

# Tạo và ghi nội dung vào các tệp tin
file = open('D:/phuc/diem.json', 'w')
file.write('day la file json')
file.close()

file1 = open('D:/phuc/thuc hanh/Bai_01.py', 'w')
file1.write('day la file py')
file1.close()

file2 = open('D:/phuc/thuc hanh/taptin.txt', 'w')
file2.write('day la file txt')
file2.close()

file3 = open('D:/phuc/thuc hanh/code.e', 'w')
file3.write('day la file e')
file3.close()

file4 = open('D:/phuc/ly thuyet/chap_01.txt', 'w')
file4.write('day la file txt')
file4.close()

file5 = open('D:/phuc/ly thuyet/final.txt', 'w')
file5.write('day la file txt')
file5.close()

file6 = open('D:/phuc/thuc hanh/th_b2_kq.txt', 'w')
file6.write('day la file thuc hanh 2')
file6.close()

file7 = open('D:/phuc/thuc hanh/th_b1_kq.txt', 'w')
file7.write('day la file thuc hanh nuoi 1')
file7.close()


print("Đã tạo xong các folder và file cần thiết")