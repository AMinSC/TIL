def solution(ineq, eq, n, m):
    if eq == "!":
        total = str(n) + ineq + str(m)
    else:
        total = str(n) + ineq + eq + str(m)
    return int(eval(total))