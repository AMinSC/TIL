def solution(data, ext, val_ext, sort_by):
    exts = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    filter_data = list(filter(lambda x: x[exts[ext]] < val_ext, data))
    return sorted(filter_data, key=lambda x: x[exts[sort_by]])