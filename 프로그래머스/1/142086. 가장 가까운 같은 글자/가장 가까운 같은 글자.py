def solution(s):
    answer = []
    s_list = []
    for i in s:
        if i not in s_list:
            answer.append(-1)
            s_list.append(i)
        elif i in s_list:
            answer.append(s_list[::-1].index(i) + 1)
            s_list.append(i)
    return answer