n = int(input())
num_list = list(map(int, input().split()))
new_avg = []
for i in num_list:
    new_avg.append(i / max(num_list) * 100)
answer = sum(new_avg) / n
print(answer)