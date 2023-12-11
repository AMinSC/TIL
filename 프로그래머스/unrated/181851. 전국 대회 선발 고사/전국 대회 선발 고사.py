def solution(rank, attendance):
    n_rank = {}
    for i in range(len(rank)):
        if attendance[i]:
            n_rank[i] = rank[i]
    answer = sorted(n_rank.items(), key=lambda x:x[1])
    return 10000 * answer[0][0] + 100 * answer[1][0] + answer[2][0]