_, s = map(int, input().split())
score_list = list(map(int, input().split()))
print(sorted(score_list, reverse=True)[s - 1])