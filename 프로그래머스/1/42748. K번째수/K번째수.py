def solution(array, commands):
    answer = []
    for i in commands:
        num_list = array[i[0] - 1: i[1]]
        num_list = sorted(num_list)
        answer.append(num_list[i[2] - 1])
    return answer