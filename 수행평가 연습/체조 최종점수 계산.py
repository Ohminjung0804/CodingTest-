'''
체조선수는 여러 심사위원의 점수 중 가장 높은 점수 하나와 가장 낮은 점수 하나를 제외하고 나머지 점수들의 평균을 계산하여 최종점수를 받습니다.
단, 이때 소수점 이하의 수는 버립니다.



매개변수 설명
심사위원이 준 점수가 들어있는 리스트 scores가 solution 함수의 매개변수로 주어집니다.
* scores의 길이는 3 이상 100 이하입니다.
* 심사위원이 부여하는 점수의 범위는 0 이상 100 이하의 정수입니다.

return 값 설명
심사위원이 준 점수 중 가장 높은 점수와 가장 낮은 점수를 제외한 점수의 평균에서 소수점을 버린 값을 return 합니다.

예시
| scores                               	| return |
|-----------------------------------------|--------|
| [35, 28, 98, 34, 20, 50, 85, 74, 71, 7] | 49 	|
| [1, 1, 1, 1, 1]                     	| 1  	|

예시 설명
예시 #1
문제에 나온 예와 같습니다.

예시 #2
가장 높은 점수는 1점이며, 가장 낮은 점수도 1점입니다. 1점을 두 개 제외한 나머지 점수의 합은 3점이며, 평균은 1점이 됩니다.

'''
import math

def solution(scores):
    return (sum(scores) - max(scores) - min(scores)) // (len(scores)-2)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
