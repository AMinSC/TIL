def solution(X, Y):
    answer = ''
    new_x = {n: X.count(n) for n in set(X)}
    new_y = {n: Y.count(n) for n in set(Y)}
    
    for k in new_x.keys():
        if k in new_y:
            answer += (k * min(new_x[k], new_y[k]))
    
    if not answer:
        return "-1"
    elif len(set(answer)) == 1 and "0" in set(answer):
        return "0"
    
    answer = sorted([n for n in answer], reverse=True)
    
    return ''.join(answer)