def solution(x):
    return not bool(x % sum(map(int, str(x))))