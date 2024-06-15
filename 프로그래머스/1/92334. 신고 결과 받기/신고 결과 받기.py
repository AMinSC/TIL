def solution(id_list, report, k):
    answer = {name: 0 for name in id_list}
    
    respondent = {}
    for names in report:
        rep, res = names.split()
        
        # 피신고자를 누가 신고했는지 체크
        if res in respondent:
            respondent[res].append(rep)
        else:
            respondent[res] = [rep]
    
    # 제재대상 선별
    targets = {res: rep for res, rep in respondent.items() if len(set(rep)) >= k}
    
    # 신고자들 메일 발송
    ## 제재 대상이 없을 경우
    if not targets:
        return [0 for _ in id_list]
    
    # 중복값 제거
    set_target = {res: set(names) for res, names in targets.items()}
    
    for _, names in set_target.items():
        for name in names:
            answer[name] += 1
            
    return [name for _, name in answer.items()]