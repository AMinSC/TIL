num_list = []
for i in range(9):
    num_col =  list(map(int, input().split()))
    num_list.extend(num_col)

list_max = max(num_list)
list_idx = num_list.index(list_max)
print(list_max)
print((list_idx // 9) + 1, (list_idx % 9) + 1, end='')
