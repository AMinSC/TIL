def solution(arr, idx):
    if sum(arr[idx:]) < 1:
        return -1
    return arr[idx:].index(1) + idx