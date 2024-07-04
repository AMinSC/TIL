def solution(before, after):
    for c in after:
        before = before.replace(c, "", 1)
    return 1 if not before else 0