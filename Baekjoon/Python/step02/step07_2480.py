f_dice, s_dice, t_dice = map(int, input().split())

if f_dice == s_dice == t_dice:
	print(10000 + f_dice * 1000)
elif f_dice == s_dice != t_dice:
	print(1000 + f_dice * 100)
elif f_dice == t_dice != s_dice:
	print(1000 + f_dice * 100)
elif s_dice == t_dice != f_dice:
	print(1000 + s_dice * 100)
elif f_dice != s_dice != t_dice:
	dice = f_dice, s_dice, t_dice
	print(max(dice) * 100)
