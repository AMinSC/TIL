"""사목, 작성자: Al Sweigart al@inventwithpython.com
입체사목과 유사한, 타일을 떨어뜨려서 4개를 한 줄로 늘어놓는 게임"""

import sys


# 말판을 표시하기 위해 사용되는 상수
EMPTY_SPACE = "."  # 마침표가 공백보다 훨씬 더 세기 편하다.
PLAYER_X = "X"
PLAYER_O = "O"

# 참고: BOARD_WIDTH가 변경될 경우에 BOARD_TEMPLATE과 COLUMN_LABELS도 갱신한다.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# 말판을 표시하기 위한 템플릿 문자열
BOARD_TEMPLATE = """
    +1234567+
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""


def main():
    """사목 게임을 실행한다."""
    print(
        """사목, 작성자: Al Sweigart al@inventwithpython.com
        
        두 사람이 차례로 7개 열 중 하나에 타일을 떨어뜨려
        수평, 수직, 대각선으로 사목을 만든다.
        """
    )

    # 새로운 게임을 설정한다.
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:  # 플레이어의 턴 실행
        # 말판을 표시하고 플레이어의 움직임 명령을 받는다.
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # 승리인지 무승부인지 확인한다.
        if is_winner(player_turn, game_board):
            display_board(game_board)  # 마지막으로 말판을 표시한다.
            print("플레이어 {}의 승리!".format(player_turn))
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)  # 마지막으로 말판을 표시한다.
            print("무승부 게임입니다!")
            sys.exit()

        # 다른 플레이어로 턴을 변경한다.
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


def get_new_board():
    """사목 말판을 표현하는 딕셔너리를 반환한다.

    키는 두 정수로 구성된 (column_index, row_index) 튜플이며,
    값은 "X", "O", "."(빈칸) 문자열이다."""
    board = {}
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMPTY_SPACE

    return board


def display_board(board):
    """화면에 말판과 타일을 표시한다."""

    # 말판 템플릿용으로 format() 문자열 메소드에 전달할 리스트를 준비한다.
    # 리스트는 말판에서 왼쪽에서 오른쪽으로, 위에서 아래 방향으로 나열된 타일
    # 전체를(빈칸을 포함해) 담고 있다.
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[column_index, row_index])

    # 말판을 표시한다.
    print(BOARD_TEMPLATE.format(*tile_chars))


def get_player_move(player_tile, board):
    """플레이어가 말판에서 타일을 떨어뜨릴 열을 선택하게 한다.

    타일이 떨어질 (column, row) 튜플을 반환한다."""
    while True:  # 플레이어가 유효한 움직임 명령을 입력할 때까지 계속 요청한다.
        print(f"플레아어 {player_tile}, 1에서 {BOARD_WIDTH}까지 숫자 또는 QUIT를 입력하십시오:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("즐겁게 퍼즐을 풀어주셔서 감사합니다!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"1에서 {BOARD_WIDTH}까지 숫자를 입력해주십시오.")
            continue  # 플레이어에게 움직임 명령을 다시 요청한다.

        column_index = int(response) - 1  # 0기반의 열 인덱스이므로 1을 뺀다(-1)

        # 가득 찬 열이면, 움직임 명령을 다시 요청한다.
        if board[column_index, 0] != EMPTY_SPACE:
            print("열이 꽉 차 있으므로, 다른 열을 선택해주십시오.")
            continue  # 플레이어에게 움직임 명령을 다시 요청한다.

        # 하단에서 시작해, 첫 번째 빈칸을 찾는다.
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[column_index, row_index] == EMPTY_SPACE:
                return column_index, row_index


def is_full(board):
    """'board'에 빈칸이 없으면 True를 반환한다.
    그렇지 않으면 False를 반환한다."""
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False  # 빈칸을 발견했으므로, False를 반환한다.

    return True  # 모든 칸이 꽉 차 있다.


def is_winner(player_tile, board):
    """'player_tile'이 'board'에서 사목을 완성하면 True를 반환하고,
    그렇지 않으면 False를 반환한다."""

    # 말판 전체를 살펴보면서, 사목을 확인한다.
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # 오른쪽으로 가면서 사목을 확인한다.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # 아래로 가면서 사목을 확인한다.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # 대각선 오른쪽 아래로 가면서 사목을 확인한다.
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

            # 대각선 왼쪽 아래로 가면서 사목을 확인한다.
            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    return False


# 이 프로그램이 (임포트하지 않고) 실행되면, 게임을 시작한다.
if __name__ == "__main__":
    main()
