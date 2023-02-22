N = int(input())
space = N - 1
for f_idx in range(1, N+1):
    print(f"{' '*space}{'*'*(f_idx*2-1)}")
    space -= 1
space = 1
for f_idx in reversed(range(1, N)):
    print(f"{' '*space}{'*'*(f_idx*2-1)}")
    space += 1