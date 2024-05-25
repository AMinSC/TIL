def solution(n, m, section):
    answer = 1
    
    start = section[0]
    for i in section[1:]:
        if start + (m - 1) < i:
            answer += 1
            start = i
    return answer