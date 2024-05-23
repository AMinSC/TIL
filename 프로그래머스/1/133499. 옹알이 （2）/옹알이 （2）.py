def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = len(babbling)
    
    past = ""
    i = 0
    while i < answer:
        cnt = 0
        for word in words:
            if word == babbling[i][:len(word)] and past != word:
                babbling[i] = babbling[i][len(word):]
                past = word
                cnt = 0
            cnt += 1
        if cnt == 4:
            i += 1
            past = ""

    return answer - len([b for b in babbling if b])
