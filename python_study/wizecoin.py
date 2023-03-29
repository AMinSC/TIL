import collections.abc
import operator


class WizCoinException(Exception):
    """wizcoin 모듈이 잘못 사용될 경우 이 예외를 발생시킨다."""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickless, knute로 새로운 WizCoin 객체를 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    @property
    def total(self):
        """이 WizCoin 객체에 포함된 모든 동전의 가치(크넛 단위)의 총합"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + self.knuts

    def weight_in_grams(self):
        """그램 단위로 동전의 무게를 반환한다."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

    @property
    def galleons(self):
        """이 객체의 galleon 동전 숫자를 반환한다."""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException("galleons attr must be set to an int, not a"
                                   + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException("galleons attr must be a positive int, not"
                                   + value.__class__.__qualname__)
        self._galleons = value

    def __repr__(self):
        """이 객체를 다시 생성하는 표현식의 문자열을 반환한다."""
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}," \
               f"{self.knuts})"

    def __str__(self):
        """이 객체의 가독성 높은 문자열 표현식을 반환한다."""
        return f"{self.galleons}g, {self.sickles}s, {self.knuts}k"

    def __add__(self, other):
        """WizCoin 두 객체의 동전 수량을 더한다."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        return WizCoin(other.galleons + self.galleons, other.sickles +
                       self.sickles, other.knuts + self.knuts)

    def __mul__(self, other):
        """양의 정수를 동전 값에 곱한다."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # 음의 정수를 곱한다면 음의 동전 값이 나와 유효하지 않게 된다.
            raise WizCoinException("cannot multiply with negative integers")

        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __rmul__(self, other):
        """음이 아닌 정수로 동전 수량을 곱한다."""
        return self.__mul__(other)

    def __iadd__(self, other):
        """다른 WizCoin 객체를 이 객체에 더한다."""
        if not isinstance(other, WizCoin):
            return NotImplemented

        # 'self' 객체를 제자리에서 바꿔쳐서 수정한다.
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self  # 제자리 바꿔치기 이중밑줄 메소드는 거의 언제나 self를 반환한다.

    def __imul__(self, other):
        """이 객체의 galleons, sickles, knuts에 음이 아닌 정수를 곱한다."""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("cannot multiply with negative integers")

        # WizCoin 클래스는 변경가능한 객체를 만들기에, 주석처리된 아래 코드와 같이
        # 새로운 객체를 생성하지 않아야 한다.
        # return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

        # 'self' 객체를 바꿔쳐서 수정한다.
        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self  # 제자리 바꿔치기 이중밑줄 메소드는 거의 언제나 self를 반환한다.

    def _comparison_operator_helper(self, operator_func, other):
        """비교 이중밑줄 메소드를 위한 헬퍼 메소드"""

        if isinstance(other, WizCoin):
            return operator_func(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operator_func(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            other_value = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operator_func(self.total, other_value)
        elif operator_func == operator.eq:
            return False
        elif operator_func == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eq는 "EQual"의 약자
        return self._comparison_operator_helper(operator.eq, other)

    def __ne__(self, other):  # ne는 "Not Equal"의 약자
        return self._comparison_operator_helper(operator.ne, other)

    def __lt__(self, other):  # lt는 "Less Than"의 약자
        return self._comparison_operator_helper(operator.lt, other)

    def __le__(self, other):  # le는 "Less than or Equal"의 약자
        return self._comparison_operator_helper(operator.le, other)

    def __gt__(self, other):  # gt는 "Greater Than"의 약자
        return self._comparison_operator_helper(operator.gt, other)

    def __ge__(self, other):  # ge는 "Greater than or Equal"의 약자
        return self._comparison_operator_helper(operator.ge, other)


purse = WizCoin(2, 5, 10)
print(repr(purse))
print(str(purse))
print(f"My purse contains {purse}.")
