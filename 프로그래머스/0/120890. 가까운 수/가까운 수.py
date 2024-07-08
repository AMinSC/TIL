def solution(array, n):
    new_li = [(i, abs(num - n)) for i, num in enumerate(array)]
    new_li = list(filter(lambda x: x[1] <= min([num for _, num in new_li]), new_li))
    
    if len(new_li) > 1:
        new_li = sorted(new_li, key=lambda x: array[x[0]])
    
    return array[new_li[0][0]]