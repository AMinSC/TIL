def solution(s):
    new_list = s.split()
    answer = []
    for c in new_list:
        if c == "Z":
            answer = answer[:-1]
            continue
        answer.append(int(c))
    return sum(answer)