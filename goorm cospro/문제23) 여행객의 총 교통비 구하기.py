'''
여행객들의 총 교통비를 계계산하는 문제
나이가 20살 이상이면 어른 요금, 그렇지 않으면 어린이 여금을 받음
여행객이 10명 이상인 경우 어른은 10% 어린이는 20% 할인을 받음
'''
def solution(member_age, transportation):
	if transportation == 'Bus':
		adult_expense = 40000
		child_expense = 15000
	elif transportation == 'Ship':
		adult_expense = 30000
		child_expense = 13000
	elif transportation == 'Airplane':
		adult_expense = 70000
		child_expense = 45000

	if len(member_age) >= 10:
		adult_expense = adult_expense - (adult_expense * 0.1)
		child_expense = child_expense - (child_expense * 0.2)

	total_expenses = 0
	for age in member_age:
		if age >= 20:
			total_expenses += adult_expense
		else:
			total_expenses += child_expense

	return total_expenses

member_age1 = [13, 33, 45, 11, 20]
transportation1 = "Bus"
ret1 = solution(member_age1, transportation1)

print("solution 함수의 반환 값은", int(ret1), "입니다.")

member_age2 = [25, 11, 27, 56, 7, 19, 52, 31, 77, 8]
transportation2 = "Ship"
ret2 = solution(member_age2, transportation2)

print("solution 함수의 반환 값은", int(ret2), "입니다.")