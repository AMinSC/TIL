n = int(input())

factorization_list = []

fa = range(2, n + 1)
cnt = 0

while n > 1:
    if n % fa[cnt] != 0:
        cnt += 1
    else:
        n //= fa[cnt]
        factorization_list.append(fa[cnt])

for i in sorted(factorization_list):
    print(i)
