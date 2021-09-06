'''
학생들의 시험 점수가 주어졌을 때, n번 학생이 몇 등인지 구하려 합니다.
학번은 0번부터 시작하며, 시험 점수는 학번순으로 주어집니다.

매개변수 설명
학생들의 시험 점수가 번호순으로 들은 리스트 scores와 학번 n이 solution 함수의 매개변수로 주어집니다.
* scores의 길이는 1 이상 100 이하입니다.
* 점수는 0점 이상 100점 이하이며 동점자는 없습니다.
* n은 0 이상 (scores의 길이 - 1) 이하의 정수입니다.

예시
| scores           | n | result |
|------------------|---|--------|
| [20, 60, 98, 59] | 3 | 3      |

예시 설명
* 3번 학생의 점수는 59점입니다.
* 점수를 내림차순으로 정렬하면 [98, 60, 59, 20]입니다.
* 정렬된 점수에서 59는 3번째에 있습니다.

따라서 3번 학생은 3등입니다.

'''
def func_a(scores, score):
   rank = 1
   for s in scores:
       if s == score:
           return rank
       rank += 1
   return 0

def func_b(arr): #정렬
   arr.sort(reverse=True)

def func_c(arr, n): #변수에 저장
   return arr[n]

def solution(scores, n):
   s = func_c(scores, n)
   func_b(scores)
   answer = func_a(scores,s)
   return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59]
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
