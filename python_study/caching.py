import sys
from functools import lru_cache

sys.setrecursionlimit(int(1e4))
fib_arr = [0, 1]


@lru_cache(maxsize=None)  # maxsize 3과 동일하게 info가 나온다. 차이점은 캐시저장용량
def fib_recur_dp(number: int) -> int:
    if number < len(fib_arr):
        return fib_arr[number]
    else:
        fib = fib_recur_dp(number - 1) + fib_recur_dp(number - 2)
        fib_arr.append(fib)
        return fib


# Hint : lru_cache 라는 기능이 있습니다.
print(fib_recur_dp(3000))
print(fib_recur_dp.cache_info())
