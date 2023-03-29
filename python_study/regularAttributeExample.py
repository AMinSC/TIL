class ClassWithRegularAttributes:
    def __init__(self):
        self._some_attribute = "some initial value"

    @property
    def some_attribute(self):  # 이것은 "getter" 메소드다
        return self._some_attribute

    @some_attribute.setter
    def some_attribute(self, value):  # 이것은 "setter" 메소드다
        if isinstance(value, str):
            self._some_attribute = value

    @some_attribute.deleter
    def some_attribute(self):  # 이것은 "deleter" 메소드다
        del self._some_attribute


obj = ClassWithRegularAttributes()
print(obj.some_attribute)  # "some initial value"를 출력
obj.some_attribute = "change value"
print(obj.some_attribute)  # "change value"를 출력
obj._someAttribute = "re"  # 속성에 직접 접근 불가
print(obj.some_attribute)
del obj.some_attribute  # someAttribute 속성을 삭제
