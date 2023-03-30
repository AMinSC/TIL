from towerofhanoi import tower_of_hanoi
from fourinarow import four_in_a_row
from tictactoe_oop import ttt_game


def main():
    while True:
        print("게임 모음에 오신걸 환영합니다.\n1) 하노이의 탑 게임\n2) 사목 게임\n3) 틱택토 게임")
        ans = input("> 1, 2, 3")

        game_list = ['1', '2', '3']

        if ans in game_list:  # try, except 문?
            ans = int(ans)
            if 1 <= ans <= 3:
                if ans == 1:
                    tower_of_hanoi()
                elif ans == 2:
                    four_in_a_row()
                elif ans == 3:
                    ttt_game()

        else:
            print("\n올바른 입력이 아닙니다!\n다시 선택해 주세요 !\n")


if __name__ == "__main__":
    main()
