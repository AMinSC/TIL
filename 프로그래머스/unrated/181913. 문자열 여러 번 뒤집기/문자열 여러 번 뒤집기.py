def solution(my_string, queries):
    answer = ''
    l = [c for c in my_string]
    for s, e in queries:
        if s == 0:
            l[s:e + 1] = l[e::-1]
        else:
            l[s:e + 1] = l[e:s - 1:-1]
    return "".join(l)