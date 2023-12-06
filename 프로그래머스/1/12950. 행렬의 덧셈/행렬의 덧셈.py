def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sub = []
        for j in range(len(arr1[i])):
            sub.append(arr1[i][j] + arr2[i][j])
        answer.append(sub)
    return answer