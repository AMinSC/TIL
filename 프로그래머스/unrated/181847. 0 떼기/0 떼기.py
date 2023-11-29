def solution(n_str):
    if n_str[0] != "0":
        return n_str
    answer = ""
    for i, n in enumerate(n_str):
        if n == "0":
            continue
        elif n != "0":
            return n_str[i:]