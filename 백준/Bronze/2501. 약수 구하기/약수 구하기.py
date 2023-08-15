a, b = map(int, input().split())

divisor = []

for i in range(1, a + 1):
    if a % i == 0:
        divisor.append(i)

try:
    answer = divisor[b - 1]
    print(answer)
except IndexError:
    print(0)
