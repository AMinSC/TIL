def solution(s, skip, index):
    answer = ''
    asc_num = list({i for i in range(97, 123)} - {ord(skip_n) for skip_n in skip})
    
    for c in s:
        asc_len = len(asc_num)
        new_index = asc_num.index(ord(c)) + index
        
        answer += chr(asc_num[(new_index) % asc_len])
    
    return answer