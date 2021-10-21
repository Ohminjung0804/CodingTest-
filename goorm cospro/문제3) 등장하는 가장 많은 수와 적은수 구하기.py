'''
배열 안에 있는 수중 가장 많은 수가 가장 적은 수의 몇 배 더 많은지 구하는 문제
'''
def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1,2,3,3,1,3,3,2,3,2]
ret = solution(arr)
print("solution 함수의 반환 값은",ret, "입니다.")