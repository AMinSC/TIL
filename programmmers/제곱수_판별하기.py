def solution(n):
    i = 1
    while i <= n//2:
        if i * i == n:
            return 1
        i += 1
    return 2
