class Car:
    """
    Car Class
    """

    _count = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Car._count += 1

    @property
    def name(self):
        return f"Hyundai {self._name}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Invalid age")
        else:
            self._age = new_age


my_car = Car("Nyyang", 10)

print(my_car.name)
print(my_car.age)
# my_car.age = -20  # ValueError: Invalid age
my_car.age = 20  # 내부 메소드 age[setter(@age.setter)] 호출
print(my_car.age)  # 내부 메소드 age[getter(@property)] 호출

# comment : 프로퍼티 사용법에 대해 다시 한번 생각 해 보세요!
"""
answer : 프로퍼티는 이니셜라이즈에서 초기화된 변숫값들을 변경할 경우,
        연결된 모든 객체들에게 영향력(버그) 이 가기 때문에 이를 방지하고자
        암묵적으로 접근제한 룰(네이밍 컨벤션)을 정하였고,
        부득이하게 접근해야 되는 일이 생길 때 사용되는 데코레이터입니다.

        동일하게 사용되는 것처럼 보이지만, 
        실은 내부 메소드를 통해서만 변경이 되는 것입니다.
        1. 필드명(내부 변수) 변경에 제한을 주고 싶을 때,
        2. 하휘 호환성..?
        3. 메서드를 속성처럼 사용 가능..(프로퍼티를 사용하지 않을 경우,
                                    getter, setter 메소드를 별도로 호출하는 번거로움 발생)
"""
