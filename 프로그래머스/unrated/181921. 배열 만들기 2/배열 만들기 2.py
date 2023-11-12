def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        sub_answer = []
        for j in str(i):
            if j not in ["0", "5"]:
                break
            elif j in ["0", "5"]:
                sub_answer.append(str(j))
        if str(i) == "".join(sub_answer):
            answer.append(i)
    if not answer:
        return [-1]
    return answer