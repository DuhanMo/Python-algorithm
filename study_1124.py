# print("Python", "java", "javaScript", sep=" vs ", end="?") # 기본은 무조건 줄바꿈인데 end 를 설정해주면 줄바꿈대신 ?로 설정해준다
# print("무엇이 더 재밌을까요?")
#

# import sys
# # 표준 출력
# print("Python", "java", file=sys.stdout)
# # 표준에러
# print("Python", "java", file=sys.stderr)

# 시험 성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# # .items() 딕셔너리를 쌍으로 보내줌
# for subject, score in scores.items():
#     # print(subject, score)
#     # ljust 공간확보후 왼쪽정렬 rjust 공간확보후 오른쪽정렬
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
# 은행 대기 순번표
# 001, 002, 003 , ...
# for num in range(1,21):
#     # 공간확보후 남는 공간에 3을 채운다
#     print("대기번호 : " + str(num).zfill(3))

# answer = (input("아무 값이나 입력하세요 : "))
#
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 + 표시, 음수일 땐 - 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 밑줄로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호 붙이기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채우기
print("{0:^<+30,}".format(100000000000000))
# fstring 사용시 똑같음
num = 100000000000000000000
print(f"{num:_>40,}")