# tictactoe_oop.py, 객체지향 틱택토 게임

ALL_SPACE = list("123456789")  # TTTBoard 딕셔너리를 위한 키
X, O, BLANK = "X", "O", " "  # 문자열 값을 위한 상수


def main():
    """틱택토 게임을 실행합니다."""
    print("틱택토 게임에 오신 당신을 환영합니다 !")
    game_board = TTTBoard()  # TTT_board 객체를 생선한다.
    current_player, next_player = X, O  # X가 선공, O가 후공

    while True:
        print(game_board.get_board_str())  # 화면에 말판을 표시한다.

        # 플레이어가 1-9 사이 숫자를 입력할 때까지 계속해서 요청한다.
        move = 0
        while not game_board.is_valid_place(move):
            print(f"{current_player}의 움직임은? (1-9)")
            move = input()
        game_board.update_board(move, current_player)  # 움직임을 만든다

        # 게임이 끝났는지 확인한다.
        if game_board.is_winner(current_player):  # 먼저 승리를 확인한다.
            print(game_board.get_board_str())
            print(current_player + "가 승리했습니다 !")
            break
        elif game_board.is_board_full():  # 다음으로 무승부인지 확인한다.
            print(game_board.get_board_str())
            print("무승부 게임입니다 !")
            break
        current_player, next_player = next_player, current_player  # 턴을 바꾼다.
    print("즐겁게 퍼즐을 풀어주셔서 감사합니다 !")


class TTTBoard:
    def __init__(self, use_pretty_board=False, use_logging=False):
        """비어 있는 새 틱택토 말판을 생성한다."""
        self._spaces = {}  # 말판은 파이썬 딕셔너리로 표현된다.
        for space in ALL_SPACE:
            self._spaces[space] = BLANK  # 모든 칸은 비어 있는 상태로 시작된다.

    def get_board_str(self):
        """말판을 텍스트로 표현하는 문자열을 반환한다."""
        return f"""
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}  1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}  4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}  7 8 9"""

    def is_valid_place(self, space):
        """이 말판의 space가 칸을 가리키는 유효한 번호이며, 칸이 비어 있을 경우
        True를 반환한다."""
        return 0 < int(space) < 10 and (space in ALL_SPACE or self._spaces[space] == BLANK)

    def is_winner(self, player):
        """ 플레이어가 이 게임에서 승자인 경우 True를 반환한다."""
        s, p = self._spaces, player  # 편의 문법으로 더 짧은 이름을 사용한다.
        # 세 행, 세 열, 두 대각선에 걸쳐 세 개 칸이 일렬로 표시되어 있는지 확인한다.
        return ((s['1'] == s['2'] == s['3'] == p) or  # 상단에 걸쳐서
                (s['4'] == s['5'] == s['6'] == p) or  # 중단에 걸쳐서
                (s['7'] == s['8'] == s['9'] == p) or  # 하단에 걸쳐서
                (s['1'] == s['4'] == s['7'] == p) or  # 좌측열 세로로
                (s['2'] == s['5'] == s['8'] == p) or  # 중앙열 세로로
                (s['3'] == s['6'] == s['9'] == p) or  # 우측열 세로로
                (s['1'] == s['5'] == s['9'] == p) or  # 대각선
                (s['3'] == s['5'] == s['7'] == p))    # 대각선

    def is_board_full(self):
        """말판의 모든 칸이 차 있다면 True를 반환한다."""
        for space in ALL_SPACE:
            if self._spaces[space] == BLANK:
                return False  # 한 칸이라도 비어 있으면 False를 반환한다.
        return True  # 어느 칸도 비어 있지 않으면, True를 반환한다.

    def update_board(self, space, player):
        """말판의 space를 player로 설정한다."""
        self._spaces[space] = player


if __name__ == "__main__":
    main()  # 임포트하지 않고 이 모듈이 실행되면 main()을 호출한다.
