"""make for chess game with python"""
BOARD_SIZE = 8
ROWS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def board():
    """체스 8X8 말판을 만든다."""
    chess_board = [row + str(val) for val in range(1, BOARD_SIZE + 1)
                   for row in ROWS]
    # print(chess_board)  # A1, B1, C1... F8, G8, H8


def king():
    """make for king"""


def queen():
    """make for queen"""


def bishops():
    """make for bishops"""


def rooks():
    """make for rooks"""


def knights():
    """make for knights"""


def pawns():
    """make for pawns"""


def check_the_king():
    """check the king"""


def checkmate():
    """checkmate"""
