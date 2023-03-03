from functools import lru_cache

# 추가과제) 더 큰값을 계산하기 위해 StackOverflow한계치를 3000까지 늘려보세요!
fib_arr = [0, 1]

@lru_cache(maxsize=496)
def fib_recur_dp(number: int) -> int:
	if number < len(fib_arr):
		return fib_arr[number]
	else:
		fib = fib_recur_dp(number-1) + fib_recur_dp(number-2)
		fib_arr.append(fib)
		return fib
# Hint : lru_cache 라는 기능이 있습니다.
print(fib_recur_dp(3000))
