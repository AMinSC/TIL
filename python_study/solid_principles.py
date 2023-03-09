from pydantic import BaseModel


# 가게 등록 클래스
class FoodStore(BaseModel):

    def __init__(self, store_name: str, open_hours: int, close_hours: int) -> None:
        if not isinstance(store_name, str):
            raise TypeError(f"{store_name} is string.")
        elif isinstance(store_name, str):
            self._store_name = store_name

        if not isinstance(open_hours, int):
            raise TypeError(f"{open_hours} is integer.")
        elif isinstance(open_hours, int):
            self._open_hours = open_hours

        if not isinstance(close_hours, int):
            raise TypeError(f"{close_hours} is integer.")
        elif isinstance(close_hours, int):
            self._close_hours = close_hours

    # 가게 등록
    def register_store(self) -> None:
        print(f"{self._store_name}가게 등록이 완료되었습니다.")
        print(f"{self._store_name}가게의 오픈 시간은 {self._open_hours}이며,")
        print(f"마감 시간은 {self._close_hours}입니다. \n감사합니다.")


# 메뉴 등록 클래스
class Menu(FoodStore):
    def __init__(self, store_name: str, open_hours: int, close_hours: int,
                 menu_name: str, menu_price: int) -> None:
        super().__init__(store_name, open_hours, close_hours)
        self._menu_count = None
        self._menu_name = menu_name
        self._menu_price = menu_price

    # 메뉴 등록
    def menu_registration(self, menu_count) -> None:
        self._menu_count = menu_count
        print(f"{self._store_name}가게에 {self._menu_name}메뉴가 등록 완료 되었습니다.\n"
              f"{self._menu_name}메뉴의 개수는{self._menu_count}개 입니다.")
        #  store_name 변수에 메뉴(Key): 메뉴 개수(value) 형식의 Dict 생성
        self._store_name = {f"{self._menu_name}": f"{self._menu_count}"}

    # 메뉴 삭제
    def menu_remove(self) -> None:
        print(f"{self._menu_name}메뉴가 제거 되었습니다.")
        # 메뉴 등록 메소드에서 생성된 Dict에서 메뉴 제거
        self._store_name.pop(self._menu_name, f"{self._menu_name}이 없습니다.")


# 주문 관련 클래스
class Order(Menu):
    def __init__(self, store_name: str, open_hours: int, close_hours: int,
                 menu_name: str, menu_price: int):
        super().__init__(store_name, open_hours, close_hours, menu_name, menu_price)

    # 주문 하기
    def order_menu(self, order_cnt: int) -> None:
        # Menu 클래스내에 메뉴 등록 메소드에서 정의된 Dict으로 1보다 작으면 주문 불가, 1이상이면 주문
        # if self._store_name[self._menu_name] < 1:
        #     print(f"{self._store_name}가게의 {self._menu_name}메뉴는 더이상 주문이 불가능 합니다.")
        # elif self._store_name[self._menu_name] >= 1:
        #     print(f"{self._store_name}가게에서 {self._menu_name}메뉴 {order_cnt}개 주문했습니다.")
        #     self._store_name[self._menu_name] -= 1
        print(self._store_name)

    # 주문 취소
    def order_cancel(self):
        pass
