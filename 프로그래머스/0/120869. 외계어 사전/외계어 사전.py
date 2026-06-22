def solution(spell, dic):
    answer = 2
    
    for s in dic:
        word = s
        if len(s) < len(spell):
            continue
        for c in spell:
            word = word.replace(c, "", 1)
        if not word:
            answer -= 1
    return answer