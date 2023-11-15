def solution(number):
    answer = 0
    l = list(map(int, number))
    answer = sum(l) % 9
    return answer