def solution(n):
    num_cnt = 1
    while num_cnt <= n:
        if num_cnt * num_cnt == n:
            num_cnt += 1
            return num_cnt * num_cnt
        num_cnt += 1
    return -1