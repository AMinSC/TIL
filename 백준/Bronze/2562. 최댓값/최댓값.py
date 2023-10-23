n_list = []
while 1:
    try:
        a = int(input())
        n_list.append(a)
    except:
        break
max_num = max(n_list)
print(f"{max_num}\n{n_list.index(max_num) + 1}")