def solution(N, stages):
    answer = []
    fail_rate = {}
    total = len(stages)
    for i in range(1, N + 1):
        if total != 0:
            fail_rate[i] = stages.count(i) / total
            total -= stages.count(i)
        else:
            fail_rate[i] = 0
    answer = sorted(fail_rate.keys(), key=lambda x: fail_rate[x], reverse=True)
    return answer