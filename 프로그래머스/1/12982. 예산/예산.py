def solution(d, budget):
    d.sort()
    for i, v in enumerate(d):
        budget -= v
        if budget < 0:
            return i
    return len(d)