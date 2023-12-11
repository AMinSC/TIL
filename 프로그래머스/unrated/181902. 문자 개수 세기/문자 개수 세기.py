def solution(my_string):
    capital = {chr(ac): 0 for ac in range(65, 91)}
    small = {chr(ac): 0 for ac in range(97, 123)}
    capital.update(small)
    for c in my_string:
        capital[c] += 1
    return [v for v in capital.values()]