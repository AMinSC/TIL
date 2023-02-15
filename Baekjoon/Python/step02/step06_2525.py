hour, minute = map(int, input().split())
time = int(input())

if 59 >= minute + time:
	print(hour, minute + time)
elif 60 <= minute + time:
	minute += time
	cnt = 0
	while (60 <= minute):
		cnt += 1
		minute -= 60
	if 23 < hour + cnt:
		print(cnt - 1, minute)
	else:
		print(hour + cnt, minute)
