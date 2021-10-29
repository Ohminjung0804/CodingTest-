'''
N명의 후보에 대해 투표한 결과가 들어있는 배열이 있습니다.
이때, 정확히 K 표를 받은 후보는 총 몇 명인지 구하는 문제
'''

def solution(votes, N, K):
	counter = [0 for _ in range(N + 1)]
	for x in votes:
		counter[x] += 1
	answer = 0
	for c in counter:
		if c == K:
			answer += 1
	return answer

votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)
print("solution 함수의 반환 값은", ret, "입니다.")