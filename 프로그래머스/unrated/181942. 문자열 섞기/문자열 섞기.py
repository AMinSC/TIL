def solution(str1, str2):
    answer = ''
    for f, s in zip(str1, str2):
        answer += (f + s)
    return answer