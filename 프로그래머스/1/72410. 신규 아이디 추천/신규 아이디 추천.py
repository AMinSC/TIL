import re

def dot_check(li):
    if li and li[0] == '.':
        li = li[1:]
    if li and li[-1] == '.':
        li = li[:-1]
    return li

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    new_id = re.sub(r"[^\w\s\.\-]", "", new_id)
    new_id = re.sub('[\.]+', '.', new_id)
    
    new_id = dot_check(new_id)
        
    new_id = new_id[:15]
    
    new_id = dot_check(new_id)
    
    if not new_id:
        return "aaa"
    
    if len(new_id) < 3:
        new_id += (new_id[-1] * (3 - len(new_id)))
    return new_id