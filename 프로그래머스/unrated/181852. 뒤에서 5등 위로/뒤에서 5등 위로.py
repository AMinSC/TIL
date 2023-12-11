def solution(num_list):
    answer = []
    return [v for i, v in enumerate(sorted(num_list)) if i >= 5]