N, M = map(int, input().split())

baskets = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, input().split())
    i -= 1
    k -= 1
    baskets = baskets[:i] + baskets[k:j] + baskets[i:k] + baskets[j:]

print(' '.join(map(str, baskets)))
