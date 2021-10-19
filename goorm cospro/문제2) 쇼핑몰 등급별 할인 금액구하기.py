'''
A 쇼핑몰에서는 회원 등급에 따라 할인 서비스를 제공합니다. 회원 등급에 따른 할인율은 다음과 같습니다.
S등급 = 5%
G등급 = 10%
V등급 = 15%
'''


def solution(price, grade):
    answer = 0

    if grade == 'S':
        answer = price - (price * 0.05)
    elif grade == 'G':
        answer = price - (price * 0.1)
    elif grade == 'V':
        answer = price - (price * 0.15)
    return int(answer)

price1 = 2500
grade1 = 'V'
ret1 = solution(price1, grade1)

price2 = 96900
grade2 = 'S'
ret2 = solution(price2, grade2)