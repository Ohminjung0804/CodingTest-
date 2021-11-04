def solution(words, word):
    count = 0
    for i in words:
        for j in range(4):
            if i[j] != word[j]:
                count += 1

    return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")