def solution(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        i = len(s) // 2
        return s[i - 1:i + 1]