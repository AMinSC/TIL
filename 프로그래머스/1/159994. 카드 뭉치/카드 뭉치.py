def solution(cards1, cards2, goal):
    cards1_i = 0
    cards2_i = 0
    for i in range(len(goal)):
        if len(cards1) > cards1_i and cards1[cards1_i] == goal[i]: cards1_i += 1
        if len(cards2) > cards2_i and cards2[cards2_i] == goal[i]: cards2_i += 1
        if i >= cards1_i + cards2_i: return "No"
    return "Yes"