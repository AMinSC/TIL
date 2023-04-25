def rating(s: str):
    check_rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
    rating_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
                     'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P':0.0}
    for i in check_rating:
        if s == i:
            return rating_score[i]

total_score = 0.0
cnt = 0

while True:
    try:
        ans = list(map(str, input().split()))
        ans_score = float(ans[1]) * rating(ans[2])
        total_score += ans_score
        cnt += float(ans[1])
    except:
        total_score /= cnt
        break

print(total_score)
