def solution(a, d, included):
    answer = 0
    num_list = [a, ]
    for i in range(len(included)):
        new_num = num_list[i] + d
        num_list.append(new_num)
    for b, v in zip(included, num_list):
        if b:
            answer += v
    return answer