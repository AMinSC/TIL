def solution(a, b):
    answer = 0
    sum_num1 = str(a) + str(b)
    sum_num2 = 2 * a * b
    return int(sum_num1) if int(sum_num1) > sum_num2 else sum_num2