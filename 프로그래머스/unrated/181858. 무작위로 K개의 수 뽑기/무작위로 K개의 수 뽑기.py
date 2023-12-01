def solution(arr, k):
    answer = []
    for i in arr:
        if i in answer:
            continue
        elif i not in answer:
            answer.append(i)
    if k <= len(answer):
        return answer[:k]
    elif k > len(answer):
        return answer + [-1] * (k - len(answer))