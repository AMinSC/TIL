# 10952
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(a+b)


# 10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 1110
num_input = num = int(input())

cnt = 0

while True:
    num1 = num // 10
    num2 = num % 10
    num_sum = num1 + num2

    num = int(str(num2) + str(num_sum % 10))
    
    cnt += 1

    if num_input == num:
        break
print(cnt)
