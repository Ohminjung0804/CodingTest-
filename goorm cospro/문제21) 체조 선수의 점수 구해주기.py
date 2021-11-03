'''
가장 높은 점수 하나와 가장 낮은 점수 하나를 제외하고 나머지 점수들의 평균을 계산하여 푀종 점수를 구하는 문제
단, 소수점 이하의 수는 버린다.
'''

def solution(scores):
	answer = 0
	answer = (sum(scores)-max(scores)-min(scores)) // (len(scores) - 2)
	return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)
print("solution 함수의 반환 값은", ret2, "입니다.")