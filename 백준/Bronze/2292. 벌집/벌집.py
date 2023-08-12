n = int(input())

cnt = 1
h = 1

while n > h:
    h += (6 * cnt)
    cnt += 1

print(cnt)
