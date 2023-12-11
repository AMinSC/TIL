def solution(arr, delete_list):
    for n in delete_list:
        if n in arr:
            arr.remove(n)
    return arr