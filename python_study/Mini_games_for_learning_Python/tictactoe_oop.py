# tictactoe_oop.py, 객체지향 틱택토 게임
import copy
import sys

ALL_SPACE = list("123456789")  # TTTBoard 딕셔너리를 위한 키
X, O = "X", "O"  # 문자열 값을 위한 상수


def ttt_game():
    """틱택토 게임을 실행합니다."""
    print("틱택토 게임에 오신 당신을 환영합니다 !")
    if input("미니 보드를 사용하겠습니까? Y/n  > ").lower().startswith('y'):
        # game_board = MiniBoard()
        game_board = HybridBoard()  # HybridBoard 객체를 생성한다.
    else:
        # game_board = TTTBoard()  # TTT_board 객체를 생성한다.
        game_board = HintBoard()  # HintBoard객체를 생성한다.
    current_player, next_player = X, O  # X가 선공, O가 후공

    while True:
        print(game_board.get_board_str())  # 화면에 말판을 표시한다.

        # 플레이어가 1-9 사이 숫자를 입력할 때까지 계속해서 요청한다.
        while True:
            print(f"{current_player}의 움직임은? (1-9)")
            move = input("> ").upper()

            if move == "QUIT":  # 게임 종료 조건
                print("이용해 주셔서 감사합니다!")
                sys.exit()

            # 숫자가 아닌 문자가 올 경우 다시 요청
            try:
                move = int(move)
                if 1 <= move <= 9:  # 조건문을 줄이고 any() 함수로 바꿀지 고민
                    if not game_board.is_valid_place(move):
                        if game_board.duplicate_check(move):  # 말판이 비어있는지 체크
                            break
            except ValueError:
                print("숫자 1 ~ 9 선택해 주세요 !")

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
            self._spaces[space] = int(space)  # 모든 칸은 비어 있는 상태로 시작된다.

    def get_board_str(self):
        """말판을 텍스트로 표현하는 문자열을 반환한다."""
        return f"""
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']}
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']}"""

    def is_valid_place(self, space):
        """이 말판의 space가 칸을 가리키는 유효한 번호이며, 칸이 비어 있을 경우
        True를 반환한다."""
        return 0 < int(space) < 10 and (space in ALL_SPACE and self._spaces[space] == int(space))

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
            if self._spaces[space] == int(space):
                return False  # 한 칸이라도 비어 있으면 False를 반환한다.
        return True  # 어느 칸도 비어 있지 않으면, True를 반환한다.

    def update_board(self, space, player):
        """말판의 space를 player로 설정한다."""
        space = str(space)
        self._spaces[space] = player

    def duplicate_check(self, space):
        """사용자가 원하는 위치가 비어있는지 체크"""
        space = str(space)
        if self._spaces[space] == int(space):
            return True  # 위치가 비어있다면 True를 반환

        print(self.get_board_str())  # 확인을 위해 말판 출력
        print(f"이미 자리에 '{self._spaces[space]}'가 있습니다.\n비어있는 위치로 옮겨주세요!")
        return False  # 비어있지 않다면 False를 반환


class MiniBoard(TTTBoard):
    def get_board_str(self):
        """말판의 텍스트 표현을 작게 하는 문자열을 반환한다."""
        # 공백 한 칸을 '.'으로 치환한다.
        dot = '.'
        for space in ALL_SPACE:
            if self._spaces[space] == int(space):
                self._spaces[space] = dot

        board_str = f"""
        {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
        {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
        {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789"""

        # 공백 한 칸을 '.'으로 치환한다.
        for space in ALL_SPACE:
            if self._spaces[space] == dot:
                self._spaces[space] = int(space)
        return board_str


class HintBoard(TTTBoard):
    def get_board_str(self):
        """힌트가 포함된 말판을 텍스트로 표현하는 문자열을 반환한다."""
        board_str = super().get_board_str()  # TTTBoard에 있는 get_board_str()를 호출한다.

        x_can_win = False
        o_can_win = False
        original_space = self._spaces  # _spaces를 백업한다.
        for space in ALL_SPACE:  # 모든 칸을 확인한다.
            # 이 칸에서 X 이동을 시뮬레이션한다.
            self._spaces = copy.copy(original_space)
            if self._spaces[space] == int(space):
                self._spaces[space] = X
            if self.is_winner(X):
                x_can_win = True

            # 이 칸에서 O 이동을 시뮬레이션한다.
            self._spaces = copy.copy(original_space)
            if self._spaces[space] == int(space):
                self._spaces[space] = O
            if self.is_winner(O):
                o_can_win = True
        if x_can_win:
            board_str += "\nX는 한 번만 더 이동하면 승리할 수 있습니다."
        if o_can_win:
            board_str += "\nO는 한 번만 더 이동하면 승리할 수 있습니다."
        self._spaces = original_space
        return board_str


class HybridBoard(HintBoard, MiniBoard):
    pass


if __name__ == "__main__":
    ttt_game()  # 임포트하지 않고 이 모듈이 실행되면 main()을 호출한다.
    # print(HybridBoard.mro())
