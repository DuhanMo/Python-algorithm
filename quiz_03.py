# 사이트별로 비밀번호를 만들어주는 프로그램

# 예 : http://naver.com

# http:// 는 제외 ->naver.com
# 처음만나는 . 이후부분 제외 -> naver
# 남은글자중 처음 세자리+글자갯수+글자내e갯수+!로 구성

# nav51!

a = "http://google.com"

index = a.index("/")
index = a.index("/",index+1)

indexLast = a.index(".")

a = a[index+1:indexLast]
pwd = a[0:3] + str(len(a)) + str(a.count("e")) + "!"
print(pwd)

