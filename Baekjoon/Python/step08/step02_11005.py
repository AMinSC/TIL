N, B = map(int, input().split())

num_dict = {val: chr(val + 55) for val in range(10, 36)}
pure_dict = {val: str(val) for val in range(10)}

num_dict.update(pure_dict)

answer = ''
keep = []

while N >= B:
    share, remainder = divmod(N, B)
    keep.append(num_dict.get(remainder))
    N = share
keep.append(num_dict.get(N))
keep.reverse()
answer = answer.join(keep)

print(answer)
