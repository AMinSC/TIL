def solution(price, money, count):
    answer = sum([c * price for c in range(1, count + 1)])
    return answer - money if answer > money else 0