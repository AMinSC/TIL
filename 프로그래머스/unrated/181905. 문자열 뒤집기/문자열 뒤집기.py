def solution(my_string, s, e):
    if s == e:
        return my_string
    l = list(map(str, my_string))
    if s and e:
        l[s:e + 1] = l[e:s - 1:-1]
    elif e:
        l[:e + 1] = l[e::-1]
    return "".join(l)