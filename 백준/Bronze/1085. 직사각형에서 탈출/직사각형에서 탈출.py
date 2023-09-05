x, y, w, h = map(int, input().split())

square = []
for i, j in zip((x, y), (w, h)):
    a = j - i
    square.append(a)
    square.append(j - a)

print(min(square))
