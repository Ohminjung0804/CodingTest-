'''
주스 1잔을 만들려면 사과 3개와 당근 1개가 필요합니다.
그런데 키우는 토끼에게 먹이를 주기 위해 사과와 당근 종류에 상관없이 k개를 빼놓으려고 합니다.
주스는 최대한 많이 만들수록 좋습니다.

사과 개수 num_apple과 당근 개수 num_carrot, 토끼에게 줄 먹이 개수 k가 주어질 때 주스를 최대 몇 잔 만들 수 있는지 return 하도록 solution 함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

'''


def solution(num_apple, num_carrot, k):
    answer = 0

    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) < 0:
        if i % 4 == 0:
            answer += 1
        i = i + 1

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")