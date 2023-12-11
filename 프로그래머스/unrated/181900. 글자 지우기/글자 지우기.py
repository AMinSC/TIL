def solution(my_string, indices):
    l_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del l_string[i]
    return "".join(l_string)