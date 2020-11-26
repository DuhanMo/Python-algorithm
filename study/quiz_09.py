# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#          출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리
#         치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생 시키고 프로그램 종료


class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


chicken = 10
waiting = 1

while (True):
    try:
        if chicken > 1:
            print("[남은 치킨 : {0}".format(chicken))
        else:
            raise SoldOutError("재료가 소진되었습니다.")
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if not (order > 0):
            raise ValueError
        if order > chicken:  # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break
