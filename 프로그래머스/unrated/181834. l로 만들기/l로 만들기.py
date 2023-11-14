def solution(myString):
    answer = ''
    for c in myString:
        if ord(c) < ord('l'):
            answer += 'l'
        else:
            answer += c
    return answer