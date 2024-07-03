def solution(s):
    if s[0] == ")":
        return False
    
    left = 0
    right = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            right += 1
            if left < right:
                return False
    if left != right:
        return False
    return True