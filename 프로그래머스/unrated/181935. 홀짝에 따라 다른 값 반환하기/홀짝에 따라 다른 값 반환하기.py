def solution(n):
    answer = 0
    if n % 2:
        for i in range(1, n + 1, 2):
            print(i)
            answer += i
    else:
        for i in range(2, n + 1, 2):
            print(i)
            answer += (i ** 2)
    return answer