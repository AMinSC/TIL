def solution(n):
    answer = [[0] * n for _ in range(n)]
    # 1차원: 인덱스가 지나가며 숫자를 하나씩 올림
        # 인덱스의 끝에 도달하거나 숫자를 만날경우 종료
    # 2차원: 1차원 배열의 개수를 넘어가거나 숫자를 만날경우 종료
    x = 0
    y = 0
    num = 1
    pre = 'r'
    while num <= (n * n):
        if pre == 'r':
            while x < n and not answer[y][x]:
                answer[y][x] = num
                x += 1
                num += 1
            pre = 'd'
            x -= 1
            y += 1
        elif pre == 'd':
            while y < n and not answer[y][x]:
                answer[y][x] = num
                y += 1
                num += 1
            pre = 'l'
            y -= 1
            x -= 1
        elif pre == 'l':
            while x >= 0 and not answer[y][x]:
                answer[y][x] = num
                x -= 1
                num += 1
            pre = 'u'
            x += 1
            y -= 1
        elif pre == 'u':
            while y >= 0 and not answer[y][x]:
                answer[y][x] = num
                y -= 1
                num += 1
            pre = 'r'
            y += 1
            x += 1
    return answer