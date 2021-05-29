# # w -> write 쓰기 위한 목적으로 출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0 ", file=score_file)
# print("영어 : 50 ", file=score_file)
# score_file.close()

# a -> append 이미 있는 파일에 추가해서 쓴다
# score_file = open('score.txt', "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동


# score_file = open("score.txt", "r", encoding="utf8")
# while True :
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# import pickle
#
# # 인코딩설정 필요없고 b < 무조건 써줘야함
# # profile_file = open("profile.pickle", "wb")
# # profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# # profile_file.close()
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

import pickle
# close 해줄 필요없음
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요 ")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())