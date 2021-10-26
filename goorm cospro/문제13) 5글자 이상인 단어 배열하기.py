'''
단어들이 들어있는 배열에서 길이가 5이상인 단어를 배열에 들어있는 순서대로 이어 붙이는 문제
'''


def solution(words):
    answer = ''
    for i in range(0, len(words)):
        if len(words[i]) >= 4:
            answer = answer + words[i]

    if answer == '':
        return "empty"
    return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);
print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);
print("solution 함수의 반환 값은", ret2, "입니다.")