a, b, v = map(int, input().split())

cnt = (v - b) / (a - b)

print(int(cnt) if int(cnt) == cnt else int(cnt) + 1)
