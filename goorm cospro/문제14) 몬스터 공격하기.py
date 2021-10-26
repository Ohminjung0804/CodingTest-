'''
게임 캐릭터가 몬ㄴ스터와 1:1 전투를 하려 한다.
몬스터는 처음에 일정 수치의 체력을 가지고 있다
개릭터가 전투에서 이기려면 몬스터를 공격해 몬스터의 체력을 0이하로 만들어야 한다.
캐릭터는 공격 마법만 사용하며, 공격 마법은 항상 같은 데미지를 입힌다.
몬스터를 힐링 마법만을 사용하며, 힐링 마법은 항상 같은 수치로 체력을 회복한다.
둘은 항상 번갈아 가며 마법을 사용하고, 처음에는 항상 캐릭터가 먼저 공격한다.
캐릭터의 공격력 attack과 몬스터가 자신의 차례에 회복하는 체력 recovery,
몬스터의 초기 체력 hp가 매개변수로 주어질때, 몬스터를 잡기 위해서 최소 몇 번 공격해야 하는지 return 하도록 solution 함수 작성
'''

def solution(attack, recovery, hp):
	count = 0
	while(True):
		count += 1
		hp -= 30
		if hp <= 0:
			break
		hp += 10
	return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")