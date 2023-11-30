def solution(arr, flag):
    answer = []
    for num, check in zip(arr, flag):
        if check:
            answer += [num for _ in range(num * 2)]
        elif not check and answer:
            for _ in range(num):
                answer.pop()
    return answer