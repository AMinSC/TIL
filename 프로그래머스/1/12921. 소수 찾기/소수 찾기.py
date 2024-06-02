def solution(n):
    # 0부터 n까지의 숫자 리스트 생성
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0과 1은 소수가 아님
    
    # 에라토스테네스의 체 알고리즘을 통해 소수 판별
    # 1. 처음 나오는 수는 나두고
    # 2. 처음 나오는 수의 배수는 싹다 제거
    for i in range(2, (n // 2) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
                
    # 소수 개수 세기
    count = primes.count(True)
    
    return count