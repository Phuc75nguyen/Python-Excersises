#doc chuoi
s = input().strip()

#tao danh sach chua so co 2 chu so
so_co_2chuso = set()

#duyet chuoi, lay  cap so co 2 chu so
for i in range (0, len(s) -1 , 2 ):
    so_co_2chuso.add(s[i : i+2])
    
    
#chuyen thanh danh sach va sap xep
xapSep_so = sorted(map(int, so_co_2chuso))

# In các số khác nhau theo thứ tự tăng dần, cách nhau một khoảng trắng
print(" ".join(map(str, xapSep_so)))