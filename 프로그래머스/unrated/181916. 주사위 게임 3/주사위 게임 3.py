def solution(a, b, c, d):
    answer = 0
    l = [a, b, c, d]
    if a == b == c == d:
        answer += a * 1111
    elif a == b == c or a == b == d or a == c == d or b == c == d:
        for i in l:
            if l.count(i) > 1:
                p = i
            elif l.count(i) == 1:
                q = i
        answer = (10 * p + q) ** 2
    elif a == b or a == c or a == d or b == c or b == d or c == d:
        try:
            p, q = set([a, b, c, d])
            print(p, q)
            answer = (p + q) * ((p - q) * -1)
        except:
            l = [n for n in l if l.count(n) == 1]
            answer = l[0] * l[1]
    else:
        answer = min([a, b, c, d])
    return answer