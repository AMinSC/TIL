string = input()
t_len = len(string)
idx = 0
cnt = 0


def keyword_checking(st: str) -> bool:
    keywords = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for keyword in keywords:
        if st == keyword:
            return True
    return False


while idx < t_len:
    if (idx + 2) < t_len:
        if keyword_checking(string[idx:idx+3]):
            idx += 3
            cnt += 1
            continue
    if (idx + 1) < t_len:
        if keyword_checking(string[idx:idx+2]):
            idx += 2
            cnt += 1
            continue
    idx += 1
    cnt += 1


print(cnt)
