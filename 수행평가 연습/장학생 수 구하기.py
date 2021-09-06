'''
모 학교에서는 학기가 끝날 때마다 장학금을 줍니다. 이때 장학생이 몇 명인지 구하려고 합니다.
장학금을 주는 조건은 다음과 같습니다.

1. 이번 학기 성적이 80점 이상(100점 만점)이면서 석차가 상위 10% 이내인 학생
2. 이번 학기 성적이 80점 이상이면서 1등인 학생
3. 직전 학기 대비 성적이 가장 많이 오른 학생(여러 명인 경우 해당 학생 전부)

단, 동점인 학생들은 등수가 같으며, 중복 수혜는 불가합니다.

매개변수 설명
학생들의 이번 학기 성적, 지난 학기 성적이 들어있는 리스트 current_grade, last_grade가 solution 함수의 매개변수로 주어집니다.
* current_grade의 길이와 last_grade의 길이는 같으며, 길이는 1 이상 200 이하입니다.
* current_grade와 last_grade의 원소는 0 이상 100 이하인 정수입니다.

return 값 설명
장학생 수를 return 해주세요.

예시
| current_grade | last_grade | return |
|------------|------------|--------|
| [70, 100, 70, 80, 50, 95] | [35, 65, 80, 50, 20, 60] | 3 |

예시 설명
학생 수가 10명보다 적으므로, 1등이 장학금을 받습니다.
직전 학기 대비 성적이 가장 많이 오른 학생은 다음과 같이 3명입니다.

* 35 → 70점
* 65 → 100점
* 60 → 95점

이때, 두 번째 학생은 이번 학기 1등 장학금을 이미 받아 중복 수혜가 불가하고,
나머지 두 학생은 장학금을 받을 수 있습니다. 따라서 장학금을 받는 학생은 총 3명입니다.
'''
def func_a(current_grade, last_grade, rank, max_diff_grade):
   arr_length = len(current_grade)
   count = 0
   for i in range(arr_length):
       if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
           count += 1
       elif current_grade[i] >= 80 and rank[i] == 1:
           count += 1
       elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
           count += 1
   return count

def func_b(current_grade):
   arr_length = len(current_grade)
   rank = [1] * arr_length
   for i in range(arr_length):
       for j in range(arr_length):
           if current_grade[i] < current_grade[j]:
               rank[i] += 1
   return rank

def func_c(current_grade, last_grade):
   max_diff_grade = 1
   for i in range(len(current_grade)):
       max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
   return max_diff_grade

def solution(current_grade, last_grade):
   rank = func_b(current_grade)
   max_diff_grade = func_c(current_grade, last_grade)
   answer = func_a(current_grade, last_grade, rank, max_diff_grade)
   return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")