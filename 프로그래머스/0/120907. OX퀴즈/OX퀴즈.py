def solution(quiz):
    result = []
    
    for q in quiz:
        formula, answer = q.split("=")
        if eval(formula) == int(answer):
            result.append("O")
        else:
            result.append("X")
    return result