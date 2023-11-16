def solution(my_strings, parts):
    answer = ''
    for string, i in zip(my_strings, parts):
        answer += string[i[0]:i[1] + 1]
    return answer