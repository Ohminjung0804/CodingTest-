def solution(price, money):
    answer = 0
    price_sum = 0
    price_sum = sum(price)
    if price_sum <= money:
        answer = money - price_sum
    else:
        return -1
    return answer