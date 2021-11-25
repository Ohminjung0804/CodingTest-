def solution(K, words):
    # 여기에 코드를 작성해주세요.
    # answer = 0
    # memo = ''
    # space = 0
    # for word in words:
    #     if len(word) > (K - len(memo + word)+space):
    #         answer += 1
    #         memo = word
    #         space = 0
    #     else:
    #         memo += word
    #         space += 1
    #         if word == words[-1]:
    #             answer += 1
    # return answer
    answer = 1
    memol = 0
    for i in range(len(words)):
        memol += len(words[i])+1
        if(memol > K+1):
            answer += 1
            memol = len(words[i])+1
    return answer





# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 17
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(K, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

