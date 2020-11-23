# continue/break
# absent = [2, 5]
# no_book = [7]  # 책을 깜빡했어
# for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#
#         break
#     print("{0},책을 읽어봐".format(student))
# # 한줄 for
# 출석번호가  1 2 3 4, 앞에 100을  붙이기로함 -> 101,102,103,104
# student = [1, 2, 3, 4, 5]
#
# print(student)
# student = [i+100 for i in student]
# print(student)

# 학생 이름을 길이로  변환
student = ["Iron man", "Thor", "I am Groot"]
# student = [len(i) for i in student]
# print(student)

# 학생 이름을 대문자로 변환
student = [i.upper() for i in student]
print(student)

