def solution(arr):
    if 2 not in arr:
        return [-1]
    elif arr.count(2) < 2:
        return [2]
    answer = arr[arr.index(2):len(arr) - arr[::-1].index(2)]
    return answer