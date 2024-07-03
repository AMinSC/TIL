def solution(lottos, win_nums):
    answer = [7, 7]

    for number in lottos:
        if number in win_nums:
            answer[0] -= 1
            answer[1] -= 1
        elif number == 0:
            answer[0] -= 1
    return [num - 1 if num == 7 else num for num in answer]