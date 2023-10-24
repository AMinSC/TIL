N, M = map(int, input().split())
answer = [0 for _ in range(N)]
for idx in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i - 1, j):
        answer[ball] = k
for i in answer:
    print(i, end=' ')
print()