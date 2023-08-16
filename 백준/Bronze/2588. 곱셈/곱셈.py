a = int(input())
b = input()
c = 0

for i, j in zip([1, 10, 100], b[::-1]):
    j = int(j)
    c += (j * i)
    print(a * j)
print(a * c)
