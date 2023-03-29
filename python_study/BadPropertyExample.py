class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = "some initial value"

    @property
    def someAtrribute(self):
        # 'self.someAttribute here'에서 밑줄을 빼먹었는데 이는,
        # 프로퍼티를 사용해 다시 getter 메소드를 접근하게 만든다
        return self.someAttribute  # 여기서 getter를 다시 호출!

    @someAtrribute.setter
    def someAttribute(self, value):  # 이것은 "setter" 메소드다
        self._someAttribute = value


obj = ClassWithBadProperty()
print(obj.someAttribute)  # getter가  getter를 호출하는 에러