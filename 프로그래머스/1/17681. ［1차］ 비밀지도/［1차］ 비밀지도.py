def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        bool_list = [False for _ in range(n)]
        for i, c in enumerate(bin(a)[2:].rjust(n,'0')):
            if int(c):
                bool_list[i] = True
        
        for i, c in enumerate(bin(b)[2:].rjust(n,'0')):
            if int(c):
                bool_list[i] = True
        
        answer.append(''.join(['#' if d else ' ' for d in bool_list]))
    return answer