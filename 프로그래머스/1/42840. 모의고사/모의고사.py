from itertools import cycle

def solution(answers):
    answer = []
    a_cycle = cycle([1, 2, 3, 4, 5])
    b_cycle = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    c_cycle = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    ranks = [0, 0, 0]
    for i in answers:
        x = next(a_cycle)
        if x == i:
            ranks[0] += 1
        y = next(b_cycle)
        if y == i:
            ranks[1] += 1
        z = next(c_cycle)
        if z == i:
            ranks[2] += 1
    
    for i, rank in enumerate(ranks):
        if max(ranks) == rank:
            answer.append(i+1)
            
    return answer