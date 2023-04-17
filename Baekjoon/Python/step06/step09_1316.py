N = int(input())
cnt = 0

for i in range(N):
    string = input()
    ans = 0
    if len(string) == 1:
        cnt += 1
        continue
    elif len(string) == 2:
        if string[0] == string[1]:
            cnt += 1
            continue
    elif len(string) > 2:
        for s in string:
            s_cnt = string.count(s)
            if s_cnt > 1:
                first = string.index(s)
                second = string.rindex(s)
                if (second - first) != (s_cnt - 1):
                    ans = 1
                    break
    if ans == 0:
        cnt += 1

print(cnt)
