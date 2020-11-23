# def profile(name, age, main_lang):
#     print(f"이름 : {name} \t 나이: {age} \t주 사용언어 : {main_lang}")


# profile("모두한", 19, "python")
# profile("유재석", 31, "java")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="python"):
    print(f"이름 : {name} \t 나이 : {age}\t 주 사용언어 : {main_lang}")


profile("모두한")
profile("유재석", main_lang="자바")

