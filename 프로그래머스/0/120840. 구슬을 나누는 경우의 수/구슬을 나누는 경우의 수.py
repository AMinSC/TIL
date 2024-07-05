def fac(n: int) -> int:
    number = 1
    for i in range(1, n + 1):
        number *= i
        
    return number


def solution(balls, share):
    n = fac(balls)
    m = fac(share)
    nm = fac(balls - share)
    
    return n // (nm * m)