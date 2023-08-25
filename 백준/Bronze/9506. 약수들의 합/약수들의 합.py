num_list = []
while 1:
    n = int(input())
    if n == -1:
        break
    num_list.append(n)

for i in num_list:
    num = []
    for j in range(1, i):
        if i % j == 0:
            num.append(j)
    if sum(num) == i:
        print(i, end=" = ")
        answer = " + ".join(map(str, num))
        print(answer)
    else:
        print(f"{i} is NOT perfect.")
