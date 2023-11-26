def solution(numbers, n):
    answer = 0
    for num in numbers:
        if answer > n:
            return answer
        answer += num
    return answer