def solution(num_list):
    mul_num = 1
    for i in num_list:
        mul_num *= i
    square = sum(num_list) ** 2
    return 1 if mul_num < square else 0