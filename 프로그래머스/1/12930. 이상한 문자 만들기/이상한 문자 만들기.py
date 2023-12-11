def solution(s):
    answer = []
    space = []
    for i, c in enumerate(s):
        if c == " ":
            space.append([i, c])
    for ss in s.split():
        for i, c in enumerate(ss):
            if i % 2:
                answer.append(c.lower())
            else:
                answer.append(c.upper())
    for i, sp in space:
        answer.insert(i, sp)
    return "".join(answer)
        