""""Xây dựng Lớp môn học để quản lý môn học của các Sinh viên gồm các thông tin: Mã môn 
học, tên môn học, số tín chỉ và các hàm thành phần giải quyết công việc chính sau:
• Thêm một môn học
• Xóa một môn học có mã bằng X được nhập từ bàn phím
• Hiển thị thông tin môn học
• Tìm kiếm môn học: Theo tên môn học, mã môn học, số tín chỉ
• Ghi thông tin của các môn học vào tập tin monhoc.txt
• Đọc dữ liệu từ tập tin monhoc.txt"""


class MonHoc:
    def __init__(self, maMonHoc, tenMonHoc, soTinChi):
        self.maMonHoc = maMonHoc
        self.tenMonHoc = tenMonHoc
        self.soTinChi = soTinChi
    
    #Hàm __str__ trả về chuỗi thông tin môn học
    def __str__(self):
        return f"Mã: {self.maMonHoc}, Tên môn học: {self.tenMonHoc}, Số tín chỉ : {self.soTinChi}"    
      
    
class QuanLyMonHoc:
    def __init__(self):
            """khởi tạo danh sách môn học"""
            self.dsMonHoc = []
    #hàm thêm một môn học
    def themMonHoc(self, monHoc):
        self.dsMonHoc.append(monHoc)
        print("Đã thêm môn học thành công!")
        
    
    #Xóa môn học có mã X được nhập từ bàn phím
    def xoa_MonHoc(self, maMonHoc):
        """
        Xóa môn học theo mã nhập vào.
        """
        for monHoc in self.dsMonHoc:
            if monHoc.maMonHoc == maMonHoc:
                self.dsMonHoc.remove(monHoc)
                print(f"Đã xóa môn học có mã {maMonHoc}")
            return
        print(f"Không tìm thấy môn học có mã {maMonHoc}")
        
        
    #Hiển thị thông tin môn học
    def hienThiThongTin(self):
        print("Thông tin danh sách các môn học")
        for monHoc in self.dsMonHoc:
            print(monHoc)
        
        
            
    #Tìm kiếm môn học: Theo tên môn học, mã môn học, số tín chỉ
    def timKiemMH(self, timKiem):
        ketQua = [
            monHoc for monHoc in self.dsMonHoc
            if timKiem in monHoc.tenMonHoc or timKiem in monHoc.maMonHoc or str(monHoc.soTinChi) == timKiem
    ]
        if ketQua:
            print("Kết quả tìm kiếm:")
            for monHoc in ketQua:
                print(monHoc)
        else:
            print("Không tìm thấy kết quả phù hợp.")
    
    
    # Ghi thông tin của các môn học vào tập tin monhoc.txt
    def ghiThongTinMH(self, path="monhoc.txt"):
        """
        Ghi thông tin danh sách môn học vào tập tin.
        """
        with open(path, "w", encoding="utf-8") as file:
            for monHoc in self.dsMonHoc:
                file.write(f"{monHoc.maMonHoc},{monHoc.tenMonHoc},{monHoc.soTinChi}\n")
        print(f"Đã ghi thông tin vào file {path}.")

    
    
    #Đọc dữ liệu từ tập tin monhoc.txt
    def read_fielMHtxt(self, path="monhoc.txt"):
        """
        Đọc thông tin danh sách môn học từ tập tin.
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    maMonHoc, tenMonHoc, soTinChi = line.strip().split(",")
                    self.themMonHoc(MonHoc(maMonHoc, tenMonHoc, int(soTinChi)))
            print(f"Đã đọc dữ liệu từ file {path}.")
        except FileNotFoundError:
            print(f"Không tìm thấy file {path}.")
        



if __name__ == "__main__":
    #tạo đối tượng cho lớp môn học
    qlMonHoc = QuanLyMonHoc() 
    
     # Thêm môn học
    qlMonHoc.themMonHoc(MonHoc("MH001", "Giải tích", 3))
    qlMonHoc.themMonHoc(MonHoc("MH002", "Lập trình Python", 3))

    # Hiển thị danh sách môn học
    qlMonHoc.hienThiThongTin()

    # Tìm kiếm môn học
    qlMonHoc.timKiemMonHoc("Toán cao cấp")
    qlMonHoc.timKiemMonHoc("MH002")

    # Xóa môn học
    qlMonHoc.xoaMonHoc("MH001")

    # Hiển thị danh sách sau khi xóa
    qlMonHoc.hienThiThongTin()

    # Ghi thông tin vào tập tin
    qlMonHoc.ghiThongTinMH()

    # Đọc thông tin từ tập tin
    qlMonHoc.docThongTinMH()
    qlMonHoc.hienThiThongTin()