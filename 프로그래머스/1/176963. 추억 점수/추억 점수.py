def solution(name, yearning, photo):
    answer = []
    people_score = {n: s for n, s in zip(name, yearning)}
    for persons in photo:
        score = 0
        for person in persons:
            if person in people_score:
                score += people_score[person]
        answer.append(score)
    return answer