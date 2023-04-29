a_list = []
max_list = 0
for i in range(5):
    a = list(input())
    a_list.append(a)
    max_list = len(a)
    if i > 0 and len(a_list[i-1]) > max_list:
        max_list = len(a_list[i-1])

for i in range(max_list):
    for j in range(5):
        try:
            print(a_list[j][i], end='')
        except:
            pass
