def solution(my_string, alp):
    if alp in my_string:
        my_string = my_string.replace(alp, chr(ord(alp) - 32))
    return my_string