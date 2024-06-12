def solution(n, lost, reserve):
    i = 0
    while i < len(lost):
        number = lost[i]
        if number in reserve:
            lost.remove(number)
            reserve.remove(number)
        else:
            i += 1
    
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        print(i + 1, i - 1)
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    
    return n - len(lost)