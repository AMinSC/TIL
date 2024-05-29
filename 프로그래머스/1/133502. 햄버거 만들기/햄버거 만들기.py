def solution(ingredient):
    answer = 0

    check_hamburger = []
    
    for val in ingredient:
        check_hamburger.append(val)
        if check_hamburger[-4:] == [1, 2, 3, 1]:
            del check_hamburger[-4:]
            answer += 1
    return answer