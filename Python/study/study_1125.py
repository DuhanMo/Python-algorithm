# # 마린 : 공격유닛, 군인. 총을 쏠 수 있음
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력
#
# print(F"{name} 유닛이 생성되었습니다.")
# print(f"체력 {hp}, 공격력 {damage}\n")
#
# # 탱크 : 공격유닛, 탱크, 포를 솔 수 있는데 , 일반 모드/ 시즈모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print(f"{tank_name} 유닛이 생성되었습니다")
# print(f"체력 {tank_hp}, 공격력{damage}\n")
#
#
# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격 합니다. [공격력 {damage}]")
#
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
