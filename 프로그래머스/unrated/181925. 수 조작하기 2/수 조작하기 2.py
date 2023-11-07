def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        if (numLog[i - 1] + 1) == numLog[i]:
            answer += "w"
        elif (numLog[i - 1] - 1) == numLog[i]:
            answer += "s"
        elif (numLog[i - 1] + 10) == numLog[i]:
            answer += "d"
        elif (numLog[i - 1] - 10) == numLog[i]:
            answer += "a"
    return answer