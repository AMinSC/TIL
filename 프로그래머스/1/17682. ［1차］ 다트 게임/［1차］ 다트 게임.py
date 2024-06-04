def solution(dartResult):
    answer = []
    rule = {"S": 1, "D": 2, "T": 3}
    score = ""
    
    for i in dartResult:
        if i.isdigit():
            score += i
        if i in rule:
            answer.append(int(score) ** rule[i])
            score = ""
        elif i == "#":
            answer[-1] *= -1
        elif i == "*":
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
    return sum(answer)