def solution(a, b):
    return sum([num for num in range(min([a, b]), max([a, b]) + 1)])