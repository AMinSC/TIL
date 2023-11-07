def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        sub_list = []
        for i in range(s, e + 1):
            if arr[i] > k:
                sub_list.append(arr[i])
        if sub_list:
            answer.append(min(sub_list))
        else:
            answer.append(-1)
    return answer