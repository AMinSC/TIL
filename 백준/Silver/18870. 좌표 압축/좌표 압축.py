import sys

index = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

sort_num_list = sorted(list(set(num_list)))
num_table = {sort_num_list[i] : i for i in range(len(sort_num_list))}

for i in num_list:
    print(num_table[i], end=" ")