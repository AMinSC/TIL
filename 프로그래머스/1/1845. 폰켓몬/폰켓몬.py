def solution(nums):
    max_cnt = len(nums) // 2
    unique = len(set(nums))
    return unique if max_cnt >= unique else max_cnt
