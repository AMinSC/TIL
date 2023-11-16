# 메뉴
class Menu:
    _appetizer = {"양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000}
    _main_menu = {"티본스테이크": 55000, "바비큐립": 54000, "해산물파스타":35000, "크리스마스파스타": 25000}
    _dessert = {"초코케이크": 15000, "아이스크림": 5000}
    _drink = {"제로콜라": 3000, "레드와인": 60000, "샴페인": 25000}

    def __init__(self) -> None:
        pass


# 달력
def MonthCalendar(START_DAY=1, END_DAY=31, days_of_week=["금", "토", "일", "월", "화", "수", "목"]):
    from itertools import cycle

    START_DAY = 1
    END_DAY = 31

    DAYS_OF_WEEK = cycle(days_of_week)

    month_calendar = dict(zip(range(START_DAY, END_DAY + 1), DAYS_OF_WEEK))

    return month_calendar


# 이벤트 할인 및 증정
class Event:
    def __init__(self, menu) -> None:
        self.menu = menu

    def base_discount(self, day: int) -> int:
        base = 1000
        return base + (day * 100) - 100

    def weekday_discount(self, day: str, menu: str) -> int:
        if day in ["일", "월", "화", "수", "목"]:
            if menu in self.menu._dessert:
                return 2023
        return 0

    def weekend_discount(self, day: str, menu: str) -> int:
        if day in ["금", "토"]:
            if menu in self.menu._main_menu:
                return 2023
        return 0

    def special_discount(self, day: int) -> bool:
        if day in [3, 10, 17, 24, 25, 31]:
            return True
        return False

    def giveaway_event(self, total_order_amount: int) -> bool:
        if total_order_amount >= 120000:
            return True
        return False

    # 이벤트 배지 (switch/case 문 가능)
    def evnet_badge(self, total_benefit_amount: int) -> str:
        if total_benefit_amount >= 20000:
            return "산타"
        elif total_benefit_amount >= 10000:
            return "트리"
        elif total_benefit_amount >= 5000:
            return "별"
        return "없음"


menu_instance = Menu()
event_instance = Event(menu_instance)

# Now you can call the methods correctly, for example:
print(event_instance.weekday_discount("월", "초코케이크"))


# def reservation_date():  # 함수명 가제
#     date = int(input("안녕하세요! 우테코 식당 12월 이벤트 플래너입니다.\n12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)\n"))

#     menu_list = input("주문하실 메뉴를 메뉴와 개수를 알려 주세요.\n(e.g. 해산물파스타-2,레드와인-1,초코케이크-1)\n").split(",")
    
#     total_acount = 0
#     total_dis = 0
#     weekday_dis = 0
#     weekend_dis = 0
#     give = False

#     print(f"12월 {date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기!\n\n<주문 메뉴>")
#     for menu in menu_list:
#         name, count = menu.split("-")
#         if name in appetizer:
#             total_acount += appetizer[name] * int(count)
#         elif name in main_menu:
#             weekend_dis += weekday_discount(month_calendar[date], name) * int(count)
#             total_acount += main_menu[name] * int(count)
#         elif name in dessert:
#             weekday_dis += weekday_discount(month_calendar[date], name) * int(count)
#             total_acount += dessert[name] * int(count)
#         elif name in drink:
#             total_acount += drink[name] * int(count)
#         print(name, count)
#     print(f"\n<할인 전 총주문 금액>\n{total_acount:,}원")
#     if giveaway_event(total_acount):
#         print("\n<증정 메뉴>\n샴페인 1개")
#         give = True
#     elif not giveaway_event(total_acount):
#         print("\n<증정 메뉴>\n없음")
    
#     base_dis = base_discount(date)

#     print(f'''\n<혜택 내역>
# 크리스마스 디데이 할인: -{base_dis:,}원
# 평일 할인: -{weekday_dis:,}원
# 주말 할인: -{weekend_dis:,}원''')
#     if special_discount(date):
#         print("특별 할인: 1,000원")
#         total_dis += 1000
#     else:
#         print("특별 할인: 0원")

#     if give:
#         print("증정 이벤트: -25,000원")
#         total_dis += 25000
#     else:
#         print("증정 이벤트: 0원")

#     total_dis += base_dis + weekday_dis + weekend_dis


#     print(f"\n<총혜택 금액>\n-{total_dis:,}원")

#     print(f"\n<할인 후 예상 결제 금액>\n{total_acount - (total_dis - 25000):,}원")

#     badge = evnet_badge(total_dis)
#     print(f"\n<12월 이벤트 배지>\n{badge}")


# reservation_date()
