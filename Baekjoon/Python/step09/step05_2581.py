m = int(input())
n = int(input())

num_list = []

for i in range(m, n + 1):
    num = []
    if i > 1:
        for j in range(1, i):
            if i % j == 0:
                num.append(j)
        if sum(num) <= 1:
            num_list.append(i)

if num_list:
    print(sum(num_list))
    print(num_list[0])
else:
    print(-1)
