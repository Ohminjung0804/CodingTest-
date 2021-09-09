'''
A씨가 하루에 TV를 두 대 이상 트는 시간을 알아내려합니다.
A씨는 매일 세 프로그램을 시청합니다. 프로그램 방송 시간이 겹칠 때는 TV를 여러 대 켜서 모든 프로그램을 봅니다.

예를 들어 두 프로그램 방송 시간대가 겹치면 TV를 두 대 켜고, 세 프로그램 방송 시간이 겹치면 TV를 세 대 켭니다.

세 프로그램 방영 시작 시각과 끝 시각이 담긴 2차원 리스트 programs가 매개변수로 주어질 때,
하루에 TV를 2대 이상 트는 총 시간을 return 하도록 solution 함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

'''


def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i >= 2:
            answer = answer + 1
    return answer
programs = [[1, 6], [3, 5], [2, 8]]
ret = solution(programs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
