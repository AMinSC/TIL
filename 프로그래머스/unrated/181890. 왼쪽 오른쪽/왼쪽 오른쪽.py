def solution(str_list):
    if not str_list:
        return []
    if "l" in str_list and "r" in str_list:
        l_index = str_list.index("l")
        r_index = str_list.index("r")
        if l_index < r_index:
            return str_list[:l_index]
        elif l_index > r_index:
            return str_list[r_index + 1:]
    elif "l" in str_list:
        return str_list[:str_list.index("l")]
    elif "r" in str_list:
        return str_list[str_list.index("r") + 1:]
    return []