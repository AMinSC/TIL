def solution(num_list):
    odd = ''.join([str(i) for i in num_list if i % 2])
    even = ''.join([str(i) for i in num_list if i % 2 == 0])
    return int(odd) + int(even)