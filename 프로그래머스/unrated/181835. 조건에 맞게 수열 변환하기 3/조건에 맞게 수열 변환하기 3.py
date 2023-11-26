def solution(arr, k):
    return [val * k for val in arr] if k % 2 else [val + k for val in arr]