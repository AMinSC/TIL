from itertools import combinations

n, b = map(int, input().split())
num_list = list(map(int, input().split()))

com_list = list(combinations(num_list, 3))
lower_numbers = []
for number in com_list:
    sum_number = sum(number)
    if sum_number <= b:
        lower_numbers.append(sum_number)
print(max(lower_numbers))