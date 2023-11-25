def solution(num_list):
    odd_num = sum([num for idx, num in enumerate(num_list) if idx % 2])
    even_num = sum([num for idx, num in enumerate(num_list) if idx % 2 == 0])
    return odd_num if odd_num > even_num else even_num