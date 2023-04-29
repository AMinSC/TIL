N, M = map(int, input().split())
ans = 0
a_list = []
b_list = []

for _ in range(N):
    num_arr = map(int, input().split())
    a_list.extend(num_arr)
for _ in range(N):
    num_arr = map(int, input().split())
    b_list.extend(num_arr)

for i in range(N * M):
    a_list[i] += b_list[i]
    print(a_list[i], end=" ")
    if ((i+1) % M == 0) and (i+1 != (N * M)):
        print()