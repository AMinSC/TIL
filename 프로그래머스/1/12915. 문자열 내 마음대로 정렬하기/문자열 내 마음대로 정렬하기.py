def solution(strings, n):
    strings =  sorted(strings)
    return sorted(strings, key=lambda x : x[n])