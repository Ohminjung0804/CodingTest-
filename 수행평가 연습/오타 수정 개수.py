'''
영어 단어를 외우기 위해 단어를 반복하여 타이핑합니다. 그런데, 타이핑하고 보니 오타가 많습니다.
오타를 수정하려면 문자를 몇 개 바꿔야 하는지 구하려 합니다.

예를 들어, "CODE"라는 단어를 3번 타이핑했더니 ["CODE", "COED", "CDEO"] 가 적혀있었습니다.

타이핑한 단어를 담은 리스트 words와 원래 치려 한 단어인 word가 주어질 때 바꿔야 하는 문자 개수를 return 하도록 solution 함수를 완성해주세요.

매개변수 설명
타이핑한 단어를 담은 리스트 words와 원래 치려 한 단어인 word가 solution 함수의 매개변수로 주어집니다.
* word는 10개 이하의 알파벳 대문자로만 이루어진 단어입니다.
* words에 담긴 문자열의 길이는 word의 길이와 같으며 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
* words에 담긴 문자열의 개수는 15 이하 자연수입니다.

예시
| words            		 | word   | return |
|--------------------------|--------|--------|
| ["CODE", "COED", "CDEO"] | "CODE" | 5 	 |
'''
import math


def solution(words, word):
    count = 0
    for comp in words:
        for x, y in zip(comp, word):        #zip() - 동일한 갯수의 문장을 묶어줌
            if x != y:
                count = count + 1


    return count

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
