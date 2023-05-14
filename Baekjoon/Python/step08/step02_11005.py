N, B = map(int, input().split())

num_dict = {val: chr(val + 55) for val in range(10, 36)}
pure_dict = {val: str(val) for val in range(10)}

num_dict.update(pure_dict)

answer = ''
while N >= B:
    share, remainder = divmod(N, B)
    answer += num_dict.get(remainder)
    N = share
answer += num_dict.get(remainder)

print(answer)
