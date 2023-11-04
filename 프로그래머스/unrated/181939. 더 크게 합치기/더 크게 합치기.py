def solution(a, b):
    sum_num1 = str(a) + str(b)
    sum_num2 = str(b) + str(a)
        
    return int(sum_num1) if int(sum_num1) > int(sum_num2) else int(sum_num2)