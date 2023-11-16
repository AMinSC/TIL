from typing import List
import random


def user_input(check_type: str) -> int:
    while 1:
        user_number = input("숫자를 입력해주세요 : ")
        match check_type:
            case "baseball_number":
                range_error = 0
                for i in user_number:
                    if ord(i) < ord("1") or ord(i) > ord("9") or user_number.count(i) > 1:
                        range_error = 1
                        break
                if range_error or len(user_number) != 3:
                    print('입력한 값이 올바르지 않습니다. 숫자 "3개 (1 ~ 9)"까지의 수를 입력해주세요.')
                else:
                    return [int(i) for i in user_number]
            case "play_option":
                if len(user_number) > 1 or not (ord("1") <= ord(user_number) <= ord("2")):
                    print('개수가 올바르지 않습니다. 숫자 "1개 (1 ~ 2)"를 입력해주세요')
                else:
                    return int(user_number)


def game_play(user: List[int], computer: List[int]) -> int:
    strike = 0
    ball = 0

    for c, u in zip(computer, user):
        if c == u:
            strike += 1
            continue
        if u in computer:
            ball += 1
            continue
    if strike == ball == 0:
        print("낫싱")
    elif strike == 3:
        print("3스트라이크\n3개의 숫자를 모두 맞히셨습니다! 게임종료")
        return 2
    elif strike > 0 and ball == 0:
        print(f"{strike}스트라이크")
    elif ball > 0 and strike == 0:
        print(f"{ball}볼")
    else:
        print(f"{ball}볼 {strike}스트라이크")
    return 0


def baseball():
    PLAY = 1
    START = 1
    QUIT = 0
    print("숫자 야구 게임을 시작합니다.")
    computer_select = random.sample(range(1, 10), 3)

    while PLAY:
        user_select = user_input("baseball_number")
        if game_play(user_select, computer_select):

            print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
            user_answer = user_input("play_option")
            if user_answer == 1:
                PLAY = START
            elif user_answer == 2:
                PLAY = QUIT

if __name__ == "__main__":
    baseball()
