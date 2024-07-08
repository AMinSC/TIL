def solution(arr):
    arr_len = len(arr)
    el_len = len(arr[0])
    
    if arr_len > el_len:
        for ar in arr:
            ar += [0 for _ in range(arr_len - el_len)]
    elif arr_len < el_len:
        for _ in range(el_len - arr_len):
            arr.append([0 for _ in range(el_len)])

    return arr