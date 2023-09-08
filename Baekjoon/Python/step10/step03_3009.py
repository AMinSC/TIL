num_list = []

for _ in range(3):
    a, b = map(int, input().split())
    num_list.append((a, b))

new_num_list = []

for i in range(2):
    new_num_list.append(list(map(lambda x: x[i], num_list)))


print(new_num_list)
for i, j, k in new_num_list:
    if i == j:
        print(k, end='')
    elif i == k:
        print(j, end='')
    else:
        print(i, end='')
    print(' ', end='')
