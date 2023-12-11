def solution(n):
    return int("".join(sorted([num for num in str(n)], reverse=True)))