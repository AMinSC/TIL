def solution(survey, choices):
    answer = ''
    table = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    score = {n: 0 for n in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    
    for s, c in zip(survey, choices):
        if c == 4:
            continue
        elif c < 4:
            score[s[0]] += (4 - c)
        elif c > 4:
            score[s[1]] += (c - 4)
            
    for k in table:
        if score[k[0]] >= score[k[1]]:
            answer += k[0]
        elif score[k[0]] < score[k[1]]:
            answer += k[1]
        
    return answer