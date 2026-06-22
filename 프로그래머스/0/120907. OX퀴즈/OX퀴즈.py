def solution(quiz):
    answer = []
    
    for q in quiz:
        q = q.replace("=", "==")
        answer.append("O" if eval(q) else "X")
    return answer