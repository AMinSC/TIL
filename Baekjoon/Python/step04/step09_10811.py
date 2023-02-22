N, M = map(int, input().split())
answer = [val + 1 for val in range(N)]
for idx in range(M):
    i, j = map(int, input().split())
    if i == j:
        continue
    for re_idx, re_val in zip(range(i-1, j), reversed(answer[i-1:j])):
        answer[re_idx] = re_val
for i in answer:
    print(i, end=' ')
print()