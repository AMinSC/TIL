n = int(input())

num_list = list(map(int, input().split()))
cnt = 0
for i in num_list:
    if i == 1:
        continue
    num = []
    for j in range(1, i):
        if i % j == 0:
            num.append(j)
    if sum(num) <= 2:
        cnt += 1

print(cnt)
