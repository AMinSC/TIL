def solution(s):
    new_s = list(map(int, s.split()))
    
    return f'{min(new_s)} {max(new_s)}'
