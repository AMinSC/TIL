num_list = sorted(map(int, input().split()))
print(num_list)
answer = num_list[0] + num_list[1] + min(num_list[2], num_list[0] + num_list[1] - 1)
print(answer)
