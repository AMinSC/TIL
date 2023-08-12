d = int(input())

m = 1

while d > m:
    d -= m
    m += 1

if m % 2 == 0:
    print(f"{d}/{m + 1 - d}")
else:
    print(f"{m - d + 1}/{d}")
