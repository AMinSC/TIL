# ZZZZZ 36
N, B = input().split()

num = {chr(val+55): val for val in range(10, 36)}
num_2 = {chr(val+48): val for val in range(10)}


answer = 0
for idx, val in enumerate(reversed(N)):
    if int(B) > 9:
        answer += num.get(val) * (int(B) ** idx)
    else:
        answer += int(val) * (int(B) ** idx)

print(answer)
