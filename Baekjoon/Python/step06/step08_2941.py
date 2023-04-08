from typing import List

string = input()
end = len(string)
cnt = 0
idx = 0


def keyword_check(subject: List[str], i: int) -> int:
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for kw in croatia:
        if subject[i] == kw[0]:
            if subject[i + 1] == kw[1]:
                if kw == croatia[2]:
                    if subject[i + 2] == kw[2]:
                        return 3
                return 2
    return 0


while idx < end:
    ans = keyword_check(string, idx)
    if ans == 3:
        cnt += 1
        idx += 3
    elif ans == 2:
        cnt += 1
        idx += 2
    else:
        cnt += 1
        idx += 1


print(cnt)
