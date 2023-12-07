def solution(sizes):
    max_w, max_h = 0, 0
    for w, h in sizes:
        max_w = max(max_w, w, h)
        max_h = max(max_h, min(w, h))
    return max_w * max_h