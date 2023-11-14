def solution(n):
    answer = []
    while 1:
        answer.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        elif n % 2:
            n = 3 * n + 1
    return answer