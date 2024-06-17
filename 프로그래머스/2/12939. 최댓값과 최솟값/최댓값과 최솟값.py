def solution(s):
    num_cp = [int(number) for number in s.split()]
    new_s = [c for c in s.split()]
    min_idx = num_cp.index(min(num_cp))
    max_idx = num_cp.index(max(num_cp))
    
    return f'{new_s[min_idx]} {new_s[max_idx]}'
