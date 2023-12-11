def solution(arr):
    i = 0
    while 2 ** i <= len(arr):
        if 2 ** i == len(arr):
            return arr
        i += 1
    arr += [0] * ((2 ** (i)) - len(arr))
    return arr