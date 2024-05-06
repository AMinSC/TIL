from itertools import combinations

def solution(numbers):
    answer = []
    for num in list(combinations(numbers, 2)):
        number = sum(num)
        if number not in answer:
            answer.append(number)
    
    return sorted(answer)