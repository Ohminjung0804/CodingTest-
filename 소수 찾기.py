# def solution(n):
#     answer = 0
#     홀수 = []
#
#     if n >= 3:
#         answer += 2
#     elif n < 3:
#         return 1
#
#     for i in range(4, n + 1):
#         if i % 3 != 1:
#             홀수.append(i)
#
#     for i in 홀수:
#         if i % 3 != 0:
#             answer += 1
#     return answer

def solution(n):
    #2부터 n까지의 숫자 배열 만들기
    num_set = set(range(2, n+1))

    for i in range(2, n+1):#배수 제거
        if i in num_set:
            num_set -= set(range(i*2, n+1, i))

    answer = len(num_set)

    return answer

n = 10
print(solution(n))