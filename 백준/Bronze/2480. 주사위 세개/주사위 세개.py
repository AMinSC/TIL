a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c or b == c:
    print(1000 + max(a, b, c, key=lambda x: (a, b, c).count(x)) * 100)
else:
    print(max(a, b, c) * 100)
