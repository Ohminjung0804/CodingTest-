'''
서로 다른 두 자연수 N과 M이 매개변수로 주어질 때, N부터 M까지의 자연수 중에서 짝수들의 제곱의 합을 return
'''

import math
def solution(N, M):
	answer = 0
	for i in range(N, M+1):
		if i % 2 == 0:
			answer += math.pow(i,2)
	return int(answer)

N = 4
M = 7
ret = solution(N,M)
print("solution 함수의 반환 값은 ", ret, "입니다.")