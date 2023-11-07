def solution(num_list):
    answer = 1
    if len(num_list) < 11:
        for n in num_list:
            answer *= n
    else:
        return sum([num for num in num_list if num <= 10])
    return answer