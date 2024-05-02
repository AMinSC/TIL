n = int(input())
xy_list = []
for _ in range(n):
    xy_list.append(list(map(int, input().split())))
xy_list = sorted(xy_list)
for x, y in xy_list:
    print(x, y)