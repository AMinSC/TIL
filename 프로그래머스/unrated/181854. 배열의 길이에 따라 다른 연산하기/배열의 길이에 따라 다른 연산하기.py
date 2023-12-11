def solution(arr, n):
    return [num + n if i % 2 == 0 else num for i, num in enumerate(arr)] if len(arr) % 2 else [num + n if i % 2 else num for i, num in enumerate(arr)]