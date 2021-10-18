'''
티셔츠가 사이즈별로 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 배열에 담아 return 해주세요.
'''


def solution(shirt_size):
    answer = [0, 0, 0, 0, 0, 0]

    for i in shirt_size:
        if i == 'XS':
            answer[0] += 1
        elif i == 'S':
            answer[1] += 1
        elif i == 'M':
            answer[2] += 1
        elif i == 'L':
            answer[3] += 1
        elif i == 'XL':
            answer[4] += 1
        elif i == 'XXL':
            answer[5] += 1
    return answer

shirt_size = ['XS', 'S', 'L', 'L', 'XL', 'S']
ret = solution(shirt_size)
print('solution 함수의 반환 값은', ret, '입니다.')