from random import random

i = 1
customer = 0
while i <= 50:
    random_minutes = int(random() * 46) + 5
    if 5 <= random_minutes <= 15:
        customer += 1
        status = "O"
    else:
        status = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(status, i, random_minutes))
    i += 1
print("총 탑승 승객 : {} 분".format(customer))
