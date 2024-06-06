def solution(s):
    answer = 1
    first_cha = s[0]
    other_cha = ''
    for i, c in enumerate(s[1:]):
        if len(first_cha) == len(other_cha):
            answer += 1
            first_cha = s[i + 1]
            other_cha = ''
        elif c == first_cha[0]:
            first_cha += c
        elif c != first_cha[0]:
            other_cha += c
    return answer