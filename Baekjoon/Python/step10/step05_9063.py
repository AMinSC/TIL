x = []
y = []

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

print((max(x) - min(x)) * (max(y) - min(y)))
