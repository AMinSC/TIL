def solution(participant, completion):
    parti_dict = {}
    for name in participant:
        if name in parti_dict:
            parti_dict[name] += 1
        else:
            parti_dict[name] = 1
    
    for name in completion:
        parti_dict[name] -= 1
        
    for name in parti_dict:
        if parti_dict[name] == 1:
            return name
        