while True:
    a, b, c = map(int, input().split())
    if not (a + b + c):
        break
    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
