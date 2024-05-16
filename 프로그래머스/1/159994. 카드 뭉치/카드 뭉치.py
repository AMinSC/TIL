def solution(cards1, cards2, goal):
    cnt = 0
    for i in range(len(goal)):
        if cards1 and cards1[0] == goal[i]:
            cards1.pop(0)
            cnt += 1
        if cards2 and cards2[0] == goal[i]:
            cards2.pop(0)
            cnt += 1
    if len(goal) == cnt:
        return "Yes"
    return "No"
    