def solution(keymap, targets):
    answer = []
    for target in targets:
        target_cnt = 0
        for word in target:
            word_cnt = []
            check = 0
            for key in keymap:
                if word in key:
                    word_cnt.append(key.find(word) + 1)
                else:
                    check += 1
            if len(keymap) != check:
                target_cnt += min(word_cnt)
            else:
                target_cnt = -1
                break
        answer.append(target_cnt)
    return answer