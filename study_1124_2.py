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
