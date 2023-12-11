def solution(a, b):
    answer = 0
    if a % 2 and b % 2:
        answer = a ** 2 + b ** 2
    elif a % 2 or b % 2:
        answer = 2 * (a + b)
    else:
        answer = max([a, b]) - min([a, b])
    return answer