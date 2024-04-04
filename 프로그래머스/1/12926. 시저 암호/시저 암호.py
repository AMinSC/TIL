def solution(s, n):
    answer = ''
    for i in [ord(c) for c in s]:
        if i == 32:
            answer += chr(i)
        elif 65 <= i <= 90 and i + n > 90:
            answer += chr((i + n) - 26)
        elif 97 <= i <= 122 and i + n > 122:
            answer += chr((i + n) - 26)
        else:
            answer += chr(i + n)
    return answer