def solution(a, b, c):
    answer = 1
    if a == b == c:
        for i in range(1, 4):
            answer *= a ** i + b ** i + c ** i
    elif a == b or a == c or b == c:
        for i in range(1, 3):
            answer *= a ** i + b ** i + c ** i
    else:
        answer *= a + b + c
    return answer