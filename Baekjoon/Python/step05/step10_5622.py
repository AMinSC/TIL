dial = {}
key = 65
b_num = 3
for num in range(2, 10):
	for alpha in range(key, 91):
		dial[chr(alpha)] = num
		if 7 == num:
			b_num = 19
			if b_num < len(dial):
				b_num += 3
				key += 4
				break
		if b_num < len(dial):
			b_num += 3
			key += 3
			break
call_try = list(map(str, input()))
answer = 0
for val in dial:
	for call_val in call_try:
		if val == call_val:
			answer += (dial[val] + 1)
print(answer)
# dict으로 풀어봤지만 다음에는 list로 풀어봐야겠음.
