num_list = []
for i in range(10):
	num_list.append(int(input()))
	num_list[i] = num_list[i] % 42
print(len(set(num_list)))
