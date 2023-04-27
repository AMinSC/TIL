def rating(s: str) -> int:
    rating_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
                     'D+': 1.5, 'D0': 1.0, 'F': 0.0}
    return rating_score[s]

total_score = 0.0
cnt = 0

while True:
    try:
        ans = list(map(str, input().split()))
        if ans[2] != 'P':
            total_score += float(ans[1]) * rating(ans[2])
            cnt += float(ans[1])
    except:
        if cnt == 0:
            break
        total_score /= cnt
        break

print('%.6f' % (total_score))
