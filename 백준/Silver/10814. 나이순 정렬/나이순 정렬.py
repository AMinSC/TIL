register_list = []
for i in range(int(input())):
    age, name = input().split()
    register_list.append([int(age), name])

for user in sorted(register_list, key=lambda x: x[0]):
    print(*user)