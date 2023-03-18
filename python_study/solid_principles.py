import abc


# 가게 등록 클래스
class FoodStore(metaclass=abc.ABCMeta):

    # 가게 등록
    @abc.abstractmethod
    def register_store(self):
        pass


# 메뉴 등록 클래스
class Menu(FoodStore):
    def __init__(self, store_name: str, open_hours: int, close_hours: int):
        self.menu_count = None
        self.menu_name = None
        self._menu_check = None
        self._store_name = store_name
        self._open_hours = open_hours
        self._close_hours = close_hours

    def register_store(self):
        print(f"{self._store_name}가게 등록이 완료되었습니다.")
        print(f"{self._store_name}가게의 오픈 시간은 {self._open_hours}이며,")
        print(f"마감 시간은 {self._close_hours}입니다. \n감사합니다.")

    # 메뉴 등록
    def menu_registration(self, menu_name: str, menu_count: int):
        self.menu_name = menu_name
        self.menu_count = menu_count
        print(f"{self._store_name}가게에 {self.menu_name}메뉴가 등록 완료 되었습니다.\n"
              f"{self.menu_name}메뉴의 개수는{self.menu_count}개 입니다.")
        #  store_name 변수에 메뉴(Key): 메뉴 개수(value) 형식의 Dict 생성
        self._menu_check = {f"{self.menu_name}": self.menu_count}
        return self._menu_check

    # 메뉴 삭제
    def menu_remove(self) -> None:
        print(f"{self.menu_name}메뉴가 제거 되었습니다.")
        # 메뉴 등록 메소드에서 생성된 Dict에서 메뉴 제거
        self._menu_check.pop(self.menu_name, f"{self.menu_name}이 없습니다.")


# 주문 관련 클래스
class Order(Menu):
    def __init__(self, store_name: str, open_hours: int, close_hours: int,
                 menu_name: str, menu_price: int):
        super().__init__(store_name, open_hours, close_hours)
        self.menu_price = menu_price
        self._menu_name = menu_name
        self._order_dict = None

    # 주문 하기
    def order_menu(self, order_dict, order_cnt: int):
        self._order_dict = order_dict

        # Menu 클래스내에 메뉴 등록 메소드에서 정의된 Dict으로 1보다 작으면 주문 불가, 1이상이면 주문
        if self._order_dict[self._menu_name] < order_cnt:
            print(f"{self._store_name}가게의 {self._menu_name}메뉴는 더이상 주문이 불가능 합니다.")
        elif self._order_dict[self._menu_name] >= order_cnt:
            print(f"{self._store_name}가게에서 {self._menu_name}메뉴 {order_cnt}개 주문했습니다.")
            self._order_dict[self._menu_name] -= order_cnt
        print(self._order_dict)

    # 주문 취소
    def order_cancel(self):
        pass


if __name__ == "__main__":
    # 가게 등록
    bbq_chicken = Menu("BBQ", 10, 22)
    bbq_chicken.register_store()

    # 메뉴랑 메뉴 개수 등록
    bbq = bbq_chicken.menu_registration("Gold_olive_chicken", 3)

    # 등록된 메뉴 체크 후 주문
    a = Order("BBQ", 10, 22, "Gold_olive_chicken", 18000)
    a.order_menu(bbq, 2)

    # 남은 개수 이상으로 주문
    a.order_menu(bbq, 2)
