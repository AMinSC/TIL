total_price = int(input())
cnt = int(input())
sub_price = 0
while (0 < cnt):
	price, buy_cnt = map(int, input().split())
	sub_price += price * buy_cnt
	cnt -= 1

if total_price == sub_price:
	print("Yes")
else:
	print("No")
