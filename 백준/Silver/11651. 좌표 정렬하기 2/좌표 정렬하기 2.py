xy_list = [list(map(int, input().split())) for _ in range(int(input()))]

for x, y in sorted(xy_list, key=lambda x: (x[1], x[0])):
    print(x, y)