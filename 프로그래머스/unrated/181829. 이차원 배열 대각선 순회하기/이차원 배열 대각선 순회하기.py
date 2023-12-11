def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) > k:
                break
            answer += board[i][j]
    return answer