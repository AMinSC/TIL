def solution(code):
    answer = ''
    mode = False
    for i, c in enumerate(code):
        if c == "1":
            mode = not mode
            continue
        if not mode and i % 2 == 0:
            answer += c
        elif mode and i % 2 == 1:
            answer += c
    if answer:
        return answer
    else:
        return "EMPTY"