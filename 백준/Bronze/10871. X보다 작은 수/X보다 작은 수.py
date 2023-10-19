n, x = map(int, input().split())
n_list = map(int, input().split())
new_list = []
for i in n_list:
    if i < x:
        new_list.append(i)
print(*new_list)