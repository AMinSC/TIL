num_list = []
for _ in range(5):
    num_list.append(int(input()))
print(f"{sum(num_list) // 5}\n{sorted(num_list)[2]}")