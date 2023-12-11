def solution(arr):
    answer = 0
    while 1:
        check = 0
        for i in range(len(arr)):
            if arr[i] > 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                check += 1
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
                check += 1
        if not check:
            return answer
        answer += 1