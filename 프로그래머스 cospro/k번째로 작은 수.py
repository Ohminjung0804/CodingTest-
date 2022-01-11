def solution(arr, k):
    answer = list()
    for i in arr:
        for j in i:
            answer.append(j)
    answer.sort()

    return answer[k - 1]