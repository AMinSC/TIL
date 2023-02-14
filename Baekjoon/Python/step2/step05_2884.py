hour, minute = map(int, input().split())

if 45 <= minute:
	print(hour, minute - 45)
elif 45 > minute:
	if 0 == hour:
		print(23, minute + (60 - 45))
	elif 1 <= hour <= 23:
		print(hour - 1, minute + (60 - 45))
