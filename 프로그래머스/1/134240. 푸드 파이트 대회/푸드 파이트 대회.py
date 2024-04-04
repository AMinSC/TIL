def solution(food):
    answer = ''
    for i, f in enumerate(food):
        if i == 0:
            continue
        answer += f'{i}' * (f // 2)
    return answer + '0' + answer[::-1]