def solution(score):
    # 각 학생의 평균 점수를 계산하고, 리스트에 저장
    averages = [sum(s) for s in score]
    
    # 평균 점수를 내림차순으로 정렬
    sorted_averages = sorted(averages, reverse=True)
    
    # 각 학생의 등수를 계산하고, 리스트에 저장
    ranks = [sorted_averages.index(a) + 1 for a in averages]
    return ranks