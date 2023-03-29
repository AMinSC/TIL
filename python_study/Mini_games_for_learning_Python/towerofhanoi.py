"""하노이 탑, 작성자: AI Sweetheart al@inventwithpython.com
원판 더미를 움직이는 퍼즐 게임"""

import copy
import sys

TOTAL_DISKS = 5  # 원판이 많을수록 퍼즐은 더 어려워진다.

# A탑에 모든 원판이 놓인 상태로 시작한다.
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def tower_of_hanoi():
    """하노이 탑 게임을 실행한다."""
    print(
        """하노이 탑, 작성자: Al Sweetheart al@inventwithpython.com
        
        탑에 쌓인 원판을 한 번에 하나씩 다른 탑으로 이동한다.
        큰 원판은 작은 원판 위에 놓을 수 없다.
        
        추가 정보는 https://en.wikipedia.org/wiki/Tower_of_Hanoi를 참고한다.
        """
    )

    """towers 딕셔너리 키 'Z', 'X', 'C'와 탑에 쌓인 원판을 표현하는 리스트
    형태의 값을 갖고 있다.  리스트는 다양한 크기의 원판을 표현하는 정수를 포함하며,
    리스트의 시작은 탑의 가장 아래 바닥이다.  원판 다섯 개로 시작하는 게임의 경우에는
    리스트 [5, 4, 3, 2, 1]가 완성된 탑을 표현한다.
    리스트 []는 탑에 쌓인 원판이 없을을 나타낸다.  리스트 [1, 3]은 작은 원판 위에
    큰 원판이 있으며, 유효하지 않은 구성이다.  리스트 [3, 1]이 허용되는 이유는
    작은 원판이 큰 원판 상단에 올라갈 수 있기 때문이다."""
    towers = {"Z": copy.copy(SOLVED_TOWER), "X": [], "C": []}

    while True:  # 이 루프문이 한 번 순회할 때마다 한 턴을 진행한다.
        # 탑과 원판을 표시한다
        display_towers(towers)

        # 사용자에게 이동 명령을 요청한다.
        from_tower, to_tower = get_player_move(towers)

        # 맨 위 원판을 from_tower에서 to_tower로 이동한다.
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # 사용자가 퍼즐을 풀었는지 확인한다.
        if SOLVED_TOWER in (towers["X"], towers["C"]):
            display_towers(towers)  # 마지막으로 탑을 한 번 더 표시한다.
            print("퍼즐을 풀었습니다!  참 잘했습니다!")
            sys.exit()


def get_player_move(towers):
    """플레이어에게 이동 명령을 요청한다.  (from_tower, to_tower)를 반환한다."""

    while True:  # 플레이어가 유효한 이동 명령을 입력할 때까지 계속 요청한다.
        print('탑의 "시작"과 "끝"의 글자 또는 QUIT를 입력하십시오.')
        print("(예: 탑 Z에서 탑 X로 원판을 이동하려면 ZX를 입력합니다.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("즐겁게 퍼즐을 풀어주셔서 감사합니다!")
            sys.exit()

        # 사용자가 유효한 탑 문자를 입력했는지 확인한다.
        if response not in ("ZX", "ZC", "XZ", "XC", "CZ", "CX"):  # 편의성 개선 ABC -> ZXC
            print("ZX, ZC, XZ, XC, CZ, CX 중 하나를 입력하십시오.")
            continue  # 플에이어에게 이동 명령을 다시 요청한다.

        # 더 설명적인 변수 이름을 사용한다.
        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            # from 탑은 비어 있을 수 없다.
            display_towers(towers)  # 비어 있는 탑을 선택할 경우, 탑이 노출되지 않아 수정.
            print("원판이 없는 탑을 선택했습니다.")
            continue  # 플레이어에게 이동 명령을 다시 요청한다.
        elif len(towers[to_tower]) == 0:
            # 어떤 원판이라도 빈 "to" 탑으로 이동 가능하다
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("더 작은 원판에 더 큰 원판을 올릴 수 없습니다.")
            continue  # 플레이어에게 이동 명령을 다시 요청한다.
        else:
            # 유효한 움직이므로 선택된 탑을 반환한다.
            return from_tower, to_tower


def display_towers(towers):
    """세 탑에 배치된 원판을 표시한다."""

    # 세 탑을 표시한다.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["Z"], towers["X"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # 원판이 없는 빈 기둥을 표시한다.
            else:
                display_disk(tower[level])  # 원판을 표시한다.
        print()

    # 탑 이름 Z, X, C를 표시한다.
    empty_space = " " * TOTAL_DISKS
    print("{0} Z{0}{0} X{0}{0} C\n".format(empty_space))


def display_disk(width):
    """주어진 width로 원판을 표시한다.  width가 0이면 원판이 없음을 의미한다."""
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # 원판이 없는 기둥을 표시한다.
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # 원판을 표시한다.
        disk = "@" * width
        num_label = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")


# 이 프로그램이 (임포트되지 않고) 단독으로 실행되면, 게임을 시작한다.
if __name__ == "__main__":
    tower_of_hanoi()
