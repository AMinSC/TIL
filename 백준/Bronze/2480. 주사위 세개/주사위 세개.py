a, b, c = map(int, input().split())

dice = a, b, c

if a == b and b == c:
    print(10000+a*1000)
elif a == b and b != c:
    print(1000 + a *100)
elif a == c and a != b:
    print(1000 + a * 100)
elif b == c and a != b:
    print(1000 + b * 100)
else:
    print(max(dice)*100)