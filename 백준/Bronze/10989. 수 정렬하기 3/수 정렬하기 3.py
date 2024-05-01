import sys
n = int(input())
num_dict = {}
for _ in range(n):
    new_num = int(sys.stdin.readline().strip())
    if new_num in num_dict:
        num_dict[new_num] += 1
    else:
        num_dict[new_num] = 1
for k in sorted(num_dict):
    for _ in range(num_dict[k]):
        print(k)