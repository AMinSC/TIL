n, m = map(int, input().split())
answer = [i for i in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        continue
    answer[a], answer[b] = answer[b], answer[a]
print(*answer, sep=" ")