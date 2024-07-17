def solution(sides):
    max_num = max(sides)
    min_num = min(sides)
    cnt1 = len([cnt for cnt in range(max_num - min_num + 1, max_num + 1)])
    cnt2 = len([cnt for cnt in range(max_num + 1, max_num + min_num)])
    return cnt1 + cnt2