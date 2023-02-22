N, M = map(int, input().split())
answer = [val + 1 for val in range(N)]
for idx in range(M):
    i, j = map(int, input().split())
    tmp = answer[i - 1]
    answer[i - 1] = answer[j - 1]
    answer[j - 1] = tmp
for i in answer:
    print(i, end=' ')
print()