import sys

num_list = []
n = int(input())
for _ in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

for n in sorted(num_list):
    print(n)