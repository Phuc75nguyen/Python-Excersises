class ThiSinh:
    def __init__(self, id, name, theory_score, practical_score):
        self.id = id
        self.name = name
        self.theory_score = self.fix_score(theory_score)
        self.practical_score = self.fix_score(practical_score)
        self.avg_score = (self.theory_score + self.practical_score) / 2
        self.rank = self.get_rank()

    # Phương thức xử lý định dạng điểm
    def fix_score(self, score):
        score = float(score)
        if score > 10:  # Nếu điểm lớn hơn 10, chia 10
            score /= 10
        return score

    # Phương thức xác định xếp loại
    def get_rank(self):
        if self.avg_score < 5:
            return "TRUOT"
        elif self.avg_score < 8:
            return "CAN NHAC"
        elif self.avg_score <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    # Phương thức biểu diễn thông tin thí sinh
    def __str__(self):
        return f"{self.id} {self.name} {self.avg_score:.2f} {self.rank}"


# Đọc số lượng thí sinh
n = int(input())
candidates = []

# Nhập thông tin các thí sinh
for i in range(1, n + 1):
    name = input().strip()
    theory_score = input().strip()
    practical_score = input().strip()
    # Tạo đối tượng thí sinh và thêm vào danh sách
    candidate = ThiSinh(f"TS{i:02}", name, theory_score, practical_score)
    candidates.append(candidate)

# Sắp xếp danh sách theo điểm trung bình giảm dần
candidates.sort(key=lambda x: x.avg_score, reverse=True)

# In ra danh sách thí sinh
for candidate in candidates:
    print(candidate)
