# tictactoe.py, 비 객체지향 틱택토 게임
ALL_SPACE = list("123456789")  # 틱택토 말판 딕셔너리를 위한 키
X, O, BLANK = "X", "O", " "  # 문자열 값을 위한 상수


def main():
    """틱택토 게임을 실행한다."""
    print("틱택토 게임에 오신 당싱을 환영합니다.")
    game_board = get_blank_board()  # 틱택토 말판 딕셔너리를 생선한다.
    current_player, next_player = X, O  # X가 선공, O가 후공

    while True:
        print(get_board_str(game_board))  # 화면에 말판을 표시한다.

        # 플레이어가 1-9 사이 숫자를 입력할 때까지 계속해서 요청한다.
        move = 0
        while not is_valid_space(game_board, move):
            print(f"{current_player}의 움직임은? (1-9)")
            move = input()
        update_board(game_board, move, current_player)  # 움직임을 만든다.

        # 게임이 끝났는지 확인한다.
        if is_winner(game_board, current_player):  # 먼저 승리를 확인한다.
            print(get_board_str(game_board))
            print(current_player + "가 승리했습니다 !")
            break
        elif is_board_full(game_board):  # 다음으로 무승부인지 확인한다.
            print(get_board_str(game_board))
            print("무승부 게임입니다 !")
            break
        current_player, next_player = next_player, current_player  # 턴을 바꾼다.
    print("즐겁게 퍼즐을 풀어주셔서 감사합니다!")


def get_blank_board():
    """비어 있는 새 틱택토 말판을 생성한다."""
    board = {}  # 말판은 파이썬 딕셔너리로 표현한다.
    for space in ALL_SPACE:
        board[space] = BLANK  # 모든 칸은 빈 상태로 시작된다.
    return board


def get_board_str(board):
    """board를 텍스트로 표현하는 문자열을 반환한다."""
    return f"""
        {board['1']}|{board['2']}|{board['3']}  1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']}  4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']}  7 8 9"""


def is_valid_space(board, space):
    """board의 space가 유효한 칸 번호이며, 그 칸이 비어 있을 경우
     True를 반환한다."""
    return 0 < int(space) < 10 and (space in ALL_SPACE or board[space] == BLANK)


def is_winner(board, player):
    """player가 이 board에서 승자인 경우 True를 반환한다."""
    b, p = board, player  # 편의 문법으로 더 짧은 이름을 사용한다.
    # 세 행, 세 열, 두 대각선에 걸쳐 세 개 칸이 일렬로 표시되었는지 확인한다.
    return ((b['1'] == b['2'] == b['3'] == p) or  # 상단에 걸쳐서
            (b['4'] == b['5'] == b['6'] == p) or  # 중단에 걸쳐서
            (b['7'] == b['8'] == b['9'] == p) or  # 하단에 걸쳐서
            (b['1'] == b['4'] == b['7'] == p) or  # 좌측 열 세로로
            (b['2'] == b['5'] == b['8'] == p) or  # 중앙 열 세로로
            (b['3'] == b['6'] == b['9'] == p) or  # 우측 열 세로로
            (b['1'] == b['5'] == b['9'] == p) or  # 대각선
            (b['3'] == b['5'] == b['7'] == p))    # 대각선))


def is_board_full(board):
    """board의 모든 칸이 차 있다면 True를 반환한다."""
    for space in ALL_SPACE:
        if board[space] == BLANK:
            return False  # 한 칸이라도 비어 있으면 False를 반환한다.
    return True  # 어느 칸도 비어 있지 않으면, True를 반환한다.


def update_board(board, space, mark):
    """board의 space를 mark로 설정한다."""
    board[space] = mark


if __name__ == "__main__":
    main()  # 임포트하지 않고 이 모듈이 실행되면 main()을 호출한다.

