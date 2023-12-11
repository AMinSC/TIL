def solution(t, p):
    answer = 0
    i = 0
    while t[i:]:
        if t[i:len(p) + i] <= p:
            answer += 1
        i += 1
        if len(t[i:]) < len(p):
            break
    return answer