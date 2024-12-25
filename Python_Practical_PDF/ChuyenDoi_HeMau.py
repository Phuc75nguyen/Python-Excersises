"""Chuyển đổi hệ màu
Viết hàm chuyển đổi giữa các mã màu Hex, RGB, CMYK, HSL
• hex_2_rgb(str)
• hex_2_cmyk(str)
• hex_2_hsl(str)
• rgb_2_hex(r, g, b)
• rgb_2_cmyk(r, g, b)
• rgb_2_hsl(r, g, b)
• hsl_2_rgb(h, s, l)
• hsl_2_hex(h, s, l)
• hsl_2_cmyk(h, s, l)
• cmyk_2_rgb(c, m, y, k)
• cmyk_2_hsl(c, m, y, k)
• cmyk_2_hex(c, m, y, k)
Ví dụ:
hex_2_rgb(“#1D9A55”) => 29, 154, 85
hex_2_hsl(“#1D9A55”) => 146.88, 0.68, 0.36
hex_2_cmyk(“#1D9A55”) => 49, 0, 27, 40"""

from colorsys import rgb_to_hsv, hsv_to_rgb, rgb_to_hls, hls_to_rgb

# HEX to RGB
def hex_2_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return r, g, b

# HEX to CMYK
def hex_2_cmyk(hex_code):
    r, g, b = hex_2_rgb(hex_code)
    c, m, y = 1 - r / 255, 1 - g / 255, 1 - b / 255
    k = min(c, m, y)
    c = (c - k) / (1 - k) if k < 1 else 0
    m = (m - k) / (1 - k) if k < 1 else 0
    y = (y - k) / (1 - k) if k < 1 else 0
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

# HEX to HSL
def hex_2_hsl(hex_code):
    r, g, b = [x / 255.0 for x in hex_2_rgb(hex_code)]
    h, l, s = rgb_to_hls(r, g, b)
    return round(h * 360, 2), round(s * 100, 2), round(l * 100, 2)

# RGB to HEX
def rgb_2_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

# RGB to CMYK
def rgb_2_cmyk(r, g, b):
    c, m, y = 1 - r / 255, 1 - g / 255, 1 - b / 255
    k = min(c, m, y)
    c = (c - k) / (1 - k) if k < 1 else 0
    m = (m - k) / (1 - k) if k < 1 else 0
    y = (y - k) / (1 - k) if k < 1 else 0
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

# RGB to HSL
def rgb_2_hsl(r, g, b):
    r, g, b = [x / 255.0 for x in (r, g, b)]
    h, l, s = rgb_to_hls(r, g, b)
    return round(h * 360, 2), round(s * 100, 2), round(l * 100, 2)

# HSL to RGB
def hsl_2_rgb(h, s, l):
    r, g, b = hls_to_rgb(h / 360, l / 100, s / 100)
    return round(r * 255), round(g * 255), round(b * 255)

# HSL to HEX
def hsl_2_hex(h, s, l):
    r, g, b = hsl_2_rgb(h, s, l)
    return rgb_2_hex(r, g, b)

# HSL to CMYK
def hsl_2_cmyk(h, s, l):
    r, g, b = hsl_2_rgb(h, s, l)
    return rgb_2_cmyk(r, g, b)

# CMYK to RGB
def cmyk_2_rgb(c, m, y, k):
    r = 255 * (1 - c / 100) * (1 - k / 100)
    g = 255 * (1 - m / 100) * (1 - k / 100)
    b = 255 * (1 - y / 100) * (1 - k / 100)
    return round(r), round(g), round(b)

# CMYK to HSL
def cmyk_2_hsl(c, m, y, k):
    r, g, b = cmyk_2_rgb(c, m, y, k)
    return rgb_2_hsl(r, g, b)

# CMYK to HEX
def cmyk_2_hex(c, m, y, k):
    r, g, b = cmyk_2_rgb(c, m, y, k)
    return rgb_2_hex(r, g, b)


if __name__ == "__main__":
    # Các trường hợp kiểm tra

# HEX -> RGB
    print(hex_2_rgb("#1D9A55"))  # Output: (29, 154, 85)

# HEX -> HSL
    print(hex_2_hsl("#1D9A55"))  # Output: (146.88, 68.0, 36.0)

# HEX -> CMYK
    print(hex_2_cmyk("#1D9A55"))  # Output: (49, 0, 45, 40)

# RGB -> HEX
    print(rgb_2_hex(29, 154, 85))  # Output: "#1D9A55"

# RGB -> HSL
    print(rgb_2_hsl(29, 154, 85))  # Output: (146.88, 68.0, 36.0)

# RGB -> CMYK
    print(rgb_2_cmyk(29, 154, 85))  # Output: (49, 0, 45, 40)

# HSL -> RGB
    print(hsl_2_rgb(146.88, 68.0, 36.0))  # Output: (29, 154, 85)

# CMYK -> HEX
    print(cmyk_2_hex(49, 0, 45, 40))  # Output: "#1D9A55"
