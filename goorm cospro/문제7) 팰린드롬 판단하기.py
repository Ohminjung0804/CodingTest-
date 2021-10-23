'''
문장을 거꾸로 해도 철자가 같은 문장을 팰린드롭이라고 하는데
팰린드롭인 문장은 true를 반환하고 아닌 문장은 false로 반환하는 문제
'''

def solution(sentence):
	str = ''
	for c in sentence:
		if c != '.' and c != ' ':
			str += c
	size = len(str)
	for i in range(size // 2):
		if str[i] != str[size - 1 - i]:
			return False
	return True

sentence1 = "never odd or even."
ret1 = solution(sentence1)
print("solution 함수의 반환 값은", ret1, "입니다.")

sentence2 = "palindrome"
ret2 = solution(sentence1)
print("solution 함수의 반환 값은", ret2, "입니다.")