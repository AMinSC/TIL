def solution(board, moves):
    answer = 0
            
    # 인형뽑기의 번호에 맞는 값 넣어주기
    baskets = []
    new_board_len = len(board)
    for move in moves:
        i = 0
        while i < new_board_len:
            # 불필요한 row값 제거
            if sum(board[i]) == 0 and i == 0:
                del board[i]
                new_board_len = len(board)
                if new_board_len == 0:
                    break
            dol = board[i][move - 1]
            if dol != 0:
                baskets.append(dol)
                board[i][move - 1] = 0
                break
            else:
                i += 1
        
        # 스퀀스 타입으로 최근 들어간 index와 그전 index 비교해서 같을 경우 제거
        if len(baskets) > 1:
            if baskets[-1] == baskets[-2]:
                baskets = baskets[:-2]
                answer += 2
    
    return answer