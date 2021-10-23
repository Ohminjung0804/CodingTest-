'''
문장중 연속된 문자가 있다면 그 문자를 없애서 반환시키는 문제
'''

def solution(characters):
	result = ""
	result += characters[0]
	for i in range(1,len(characters)-1):
		if characters[i - 1] != characters[i]:
			result += characters[i]
	return result

characters = "senteeenccccceeee"
ret = solution(characters)
print("solution 함수의 반환 값은", ret, " 입니다.")