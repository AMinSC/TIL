from typing import Dict, List
import random


def buy_lotto(cnt: int) -> Dict[int, List[int]]:
    lotto_dict = {}

    for i in range(1, cnt + 1):
        new_lotto_list = random.sample(range(1, 46), 6)
        new_lotto_list = sorted(new_lotto_list)
        print(new_lotto_list)
        lotto_dict[i] = new_lotto_list
    
    return lotto_dict


def winning_check(lotto_list: Dict[int, List[int]]) -> Dict[int, int]:
    winning_dict = {i : 0 for i in range(1, 6)}

    winning_numbers = list(map(int, input("\n당첨 번호를 입력해 주세요.\n").split(",")))

    bonus_number = int(input("\n보너스 번호를 입력해 주세요.\n"))

    for i in lotto_list.values():
        winner_count = 0
        bonus = 0
        for j in i:
            cnt = winning_numbers.count(j)
            winner_count += cnt
            if winner_count == 5 and bonus_number in i:
                bonus += 1
        if winner_count == 3:
            winning_dict[5] += 1
        elif winner_count == 4:
            winning_dict[4] += 1
        elif winner_count == 5:
            winning_dict[3] += 1
        elif winner_count == 5 and bonus_number:
            winning_dict[2] += 1
        elif winner_count == 6:
            winning_dict[1] += 1
    
    return winning_dict


def winning_statistics(winning_list: Dict[int, int]) -> int:
    print(f"""\n당첨 통계\n---
3개 일치 (5,000원) - {winning_list[5]}개
4개 일치 (50,000원) - {winning_list[4]}개
5개 일치 (1,500,000원) - {winning_list[3]}개
5개 일치, 보너스 볼 일치 (30,000,000원) - {winning_list[2]}개
6개 일치 (2,000,000,000원) - {winning_list[1]}개""")

    total_price = 0
    for i, v in sorted(winning_list.items(), reverse=True):
        if v and i == 5:
            total_price += v * 5000
        elif v and i == 4:
            total_price += v * 50000
        elif v and i == 3:
            total_price += v * 1500000
        elif v and i == 2:
            total_price += v * 30000000
        elif v and i == 1:
            total_price += v * 2000000000

    return total_price


def lotto():
    purchase_amount = int(input("구입금액을 입력해 주세요.\n"))

    number_of_purchases = purchase_amount // 1000
    lotto_buy_list = buy_lotto(number_of_purchases)
    lotto_winning_list = winning_check(lotto_buy_list)
    total_price = winning_statistics(lotto_winning_list)

    print(f"총 수익률은 {total_price / purchase_amount}%입니다.")

if __name__ == '__main__':
    lotto()
