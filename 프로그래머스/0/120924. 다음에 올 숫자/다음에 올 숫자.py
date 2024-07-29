def solution(common):
    first = common[-1] - common[-2]
    second = common[-2] - common[-3]
    if first == second: return (common[-1] - common[-2]) + common[-1];
    else: return (common[-1] // common[-2]) * common[-1]; 