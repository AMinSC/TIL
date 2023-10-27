num_list = []
for _ in range(10):
    number = int(input())
    div_number = number % 42
    if div_number not in num_list:
        num_list.append(div_number)
print(len(num_list))