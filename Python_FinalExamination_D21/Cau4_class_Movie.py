"""Viết một lớp có tên Movies đại diện cho mỗi phim có trong kho phim. Mỗi phim có các thuộc tính sau:
title: tên phim (CHARLIE'S ANGELS), director: đạo diễn(Elizabeth Banks),
actor: diễn viên chính (Christen Stewart, Naomi Scott, Ella Balinska); year: năm phát hành  (2019), rating: điểm đánh giá phim
Lớp Movie phải có trình khởi tạo chấp nhận title, dicrector, actor, year và rating của phim làm đối số. Các giá trị này
phải được gán cho các thuộc tính tương ứng của đối tượng.

Lớp Movie cũng có các phương thức sau:
- read(): trả về 1 bộ phim gồm 2 phần tử là số lượng đạo diễn và số lượng diễn viên của phim.
__str__(): trả về một chuỗi mô tả phim này theo tên phim, year và rating (ví dụ : "Những thiên thần của Charlie sản xuất năm 2019 có điểm đánh giá là 4.5")'
"""

class Movie:
    def __init__(self,title, dicrector, actor, year,rating):
        """
        Trình khởi tạo chấp nhận các thông tin về bộ phim.
        :param title: Tên phim
        :param director: Đạo diễn
        :param actor: Danh sách diễn viên
        :param year: Năm phát hành
        :param rating: Điểm đánh giá phim
        """
        self.title = title
        self.dicrector = dicrector
        self.actor= actor
        self.year = year
        self.rating = rating
        
    def read(self):
        """
        Trả về bộ gồm:
        - Số lượng đạo diễn
        - Số lượng diễn viên
        """
        num_dicrectors = len(self.dicrector.split(","))
        num_actors = len(self.actor.split(","))
        return num_dicrectors, num_actors
    
    
    def __str__(self):
        "Trả về chuỗi mô tả thông phim của bộ phim "
        return f"{self.title} được sản xuất năm {self.year} có điểm đánh giá là {self.rating}"
    
    
#viết hàm kiểm thử
if __name__ == "__main__":
    #tạo đối tượng cho lớp Movie
    movie = Movie(
    title = "Những thiên thần của  Charlie",
    dicrector = "Elizabeth Banks",
    actor = "Christen Stewart, Naomi Scott, Ella Balinska",
    year = 201,
    rating= 4.5,
    )
#gọi phương thức read()
num_dicrectors, num_actors = movie.read()
print(f"Số lượng đạo diễn: {num_dicrectors}, Số lượng diễn viên: {num_actors}")


#gọi phương thức __str__
print(movie)