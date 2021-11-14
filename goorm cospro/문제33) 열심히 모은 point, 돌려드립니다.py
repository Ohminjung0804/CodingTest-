def solution(point):
	if point < 1000:
		return 0
	return round(point,-2)

point = 2323
ret = solution(point)

print("solution 함수의 반환 값은", ret, "입니다.")