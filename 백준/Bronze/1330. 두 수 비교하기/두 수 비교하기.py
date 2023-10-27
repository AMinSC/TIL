a, b = map(int, input().split())
answer = '==' if a == b else '>' if a > b else '<'
print(answer)
