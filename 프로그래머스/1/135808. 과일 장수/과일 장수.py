def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    s, n = 0, m
    d = len(score)
    while n <= d:
        answer += min(score[s:n]) * m
        s += m
        n += m
    return answer