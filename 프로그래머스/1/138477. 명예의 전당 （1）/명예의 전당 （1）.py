def solution(k, score):
    answer = []
    dailys = []
    for i in score:
        if len(dailys) < k:
            dailys.append(i)
        else:
            dailys.append(i)
            dailys = sorted(dailys, reverse=True)[:k]
        answer.append(sorted(dailys, reverse=True)[-1])
    return answer