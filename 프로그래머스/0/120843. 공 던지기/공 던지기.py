def solution(numbers, k):
    numbers *= k
    
    return numbers[2 * (k - 1)]