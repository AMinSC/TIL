def solution(arr1, arr2):
    return [[a + b for a, b in zip(a, b)] for a, b in zip(arr1, arr2)]