import itertools

def solution(nums):
    combi_li = [sum(numbers) for numbers in itertools.combinations(nums, 3)]
    prime_li = []
    
    for i in combi_li:
        if all(i % j != 0 for j in range(2, i)):
            prime_li.append(i)
    return len(prime_li)