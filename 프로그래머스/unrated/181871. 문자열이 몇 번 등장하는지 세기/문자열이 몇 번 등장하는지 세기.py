def checked_str(s: str, c: str):
    if s == c:
        return 1
    return 0

def solution(myString, pat):
    answer = 0
    f = 0
    b = len(pat)
    while b <= len(myString):
        if checked_str(myString[f:b], pat):
            answer += 1
            f += 1
            b += 1
        else:
            f += 1
            b += 1
    return answer