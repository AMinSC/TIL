def solution(my_string, m, c):
    return "".join([c for c in my_string[c - 1::m]])