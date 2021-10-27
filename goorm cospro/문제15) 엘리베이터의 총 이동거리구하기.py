'''
하루 동안 엘리베이터가 멈춘 층이 순서대로 들어있는 배열로 엘리베이터의 총 이동거리를 구하는 문제
'''

def solution(floors):
	dist = 0
	length = len(floors)
	for i in range(1,len(floors)):
		if floors[i] > floors[i-1]:
			dist += floors[i] - floors[i-1]
		else:
			dist += floors[i-1] - floors[i]
	return dist

floors = [1, 2, 5, 4, 2]
ret = solution(floors)
print("solution 함수의 반환 값은", ret, "입니다.")