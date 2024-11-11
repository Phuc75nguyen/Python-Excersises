"""
Write a Python program to subtract five days from current date"""


from datetime import timedelta, datetime

#lấy ngày hiện tại
today = datetime.now()
sbtr5days = today - timedelta(days=5)


print("Today is:", today.strftime('%d-%m-%Y'))
print("The day after sub 5 days:", sbtr5days.strftime('%d-%m-%Y'))
"""

from datetime import datetime, timedelta

# Hàm đệ quy để trừ ngày
def subtract_days(date, days):
    if days == 0:
        return date
    return subtract_days(date - timedelta(days=1), days - 1)

# Lấy ngày hiện tại
today = datetime.now()
sbtr5days = subtract_days(today, 5)

print("Today is:", today.strftime('%d-%m-%Y'))
print("The day after sub 5 days:", sbtr5days.strftime('%d-%m-%Y'))


"""