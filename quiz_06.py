# 표준 체중을 구하시오
# 성별에 따른 공식
# 남자 : 키 * 키 * 22
# 여자 : 키 * 키 * 21

# 조건 : 표준 체중은 별도의 함수 내에서 계산
#         함수명 : std_weight
#         전달값 : (키(height), 성별(gender))
# 조건 : 표준체중은 소수점 둘째자리까지 표시
#
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    weight = 0;
    if gender == "여자":
        weight = height * height * 21 * 0.0001
    else:
        weight = height * height * 22 * 0.0001
    print(f"키 {height} {gender}의 표준 체중은 {weight:.2f} 입니다.")


std_weight(170, "여자")