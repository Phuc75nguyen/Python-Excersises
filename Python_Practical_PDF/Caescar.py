"""Bài thi thực hành E21 câu 3"""


def caesar_encrypt(plain_text, step):
    cipher_text = ""
    for char in plain_text:
        # Kiểm tra nếu là chữ cái
        if char.isalpha():
            # Xử lý chữ cái viết hoa
            if char.isupper():
                cipher_text += chr((ord(char) - ord('A') + step) % 26 + ord('A'))
            # Xử lý chữ cái viết thường
            else:
                cipher_text += chr((ord(char) - ord('a') + step) % 26 + ord('a'))
        else:
            # Giữ nguyên ký tự không phải chữ cái
            cipher_text += char
    return cipher_text

# Test hàm
plain_text = "Hello, World!"
step = 3
print(caesar_encrypt(plain_text, step))  # Kết quả: "Khoor, Zruog!"
