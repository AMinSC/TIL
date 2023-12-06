def solution(n, m):
    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
            num_1 = i
    num_2 = n * m // num_1
    return num_1, num_2