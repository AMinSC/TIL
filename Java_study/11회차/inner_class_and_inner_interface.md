# 이너 클래스와 이너 인터페이스

## 이너 클래스
클래스 내부에 포함되는 `이너 클래스(inner class)`는 인스턴스 멤버 이너 클래스, 정적 멤버 이너 클래스 그리고 지역 이너 클래스로 나뉩니다.

인스턴스 멤버와 정적 멤버 이너 클래스는 필드와 메서드처럼 클래스의 멤버인 반면, 지역 이너 클래스는 메서드 내에서 정의하며, 지역 변수처럼 해당 메서드 내부에서만 한정적으로 사용되는 클래스입니다.


### 인스턴스 멤버 이너 클래스
인스턴스 멤버 이너 클래스는 이름에서도 알 수 있는 것처럼 인스턴스, 즉 객체 내부에 멤버의 형태로 존재합니다.

이때 자신을 감싸고 있는 아우터 클래스(outer class)의 모든 접근 지정자의 멤버에 접근할 수 있습니다.
인스턴스 멤버 이너 클래스 자체도 아우터 클래스의 멤버이므로 당연합니다.

> 접근 지정자와 상관없이 아우터 클래스의 멤버를 사용할 수 있다는 점을 활용하기 위해 일반적으로 이너 클래스를 사용합니다.
따라서 이너 클래스가 아우터 클래스와 밀접하게 관련되어 있을 때 주로 사용합니다.

소스 파일(.java)이 1개라 하더라도 컴파일을 수행하면 각 클래스별로 바이트 코드(.class) 파일이 생성됩니다.  따라서 이너 클래스도 마찬가지로 `아우터 클래스$이너 클래스.class`형식으로 생성됩니다.

이너 클래스로 생성되는 파일명에서 볼 수 있는 것처럼 이너 클래스는 독립적으로 사용할 수 없고, 반드시 아우터 클래스를 이용해야만 사용할 수 있습니다.

- 인스턴스 이너 클래스 객체 생성하기
앞에서 말한 것처럼 인스턴스 멤버 이너 클래스는 아우터 클래스의 객체 내부에 존재하기 때문에 이너 클래스의 객체를 생성하기 위해서는 먼저 아우터 클래스의 객체를 생성해야 합니다.

```java
// 인스턴스 멤버 이너 클래스의 객체 생성 방법
아우터 클래스 아우터 클래스 참조 변수 = new 아우터 클래스();
아우터 클래스.이너 클래스 이너 클래스 참조 변수 = 아우터 클래스 참조 변수.new 이너 클래스();

// 예
class A {
    class B {
        ...
    }
}

A a = new A();
A.B b = a.new B();
```

여기서 한 가지 주의해야 할 점은 이너 클래스 객체의 자료형은 B가 아니라 A.B라는 것입니다.  그 이유는 생성되는 바이트 코드가 A$B.class이기 때문입니다.


- 아우터 클래스의 객체 참조하기
아우터 클래스의 필드나 메서드와 동일한 이름을 이너 클래스 안에서 정의했다면, 당연히 이너 클래스의 필드나 메서드가 참조됩니다.
참조 객체명을 생략할 때는 자기 자신의 객체를 가리키는 this 키워드를 컴파일러가 자동으로 추가하기 때문입니다.

하지만, 이너 클래스 내부에서 아우터 클래스의 멤버를 참조하고 싶다면 `아우터 클래스명.this.`를 명시적으로 붙여 사용해야 합니다.

> 이너 클래스의 메서드 내에서 참조 변수 없이 멤버를 사용하면 컴파일러는 일단 `this.`를 붙여 멤버를 찾습니다.
만일 해당되는 멤버가 없다면 `아우터 클래스.this.`를 붙여 아우터 클래스의 멤버를 검색해 실행합니다.


### 정적 멤버 이너 클래스
정적 멤버 이너 클래스는 이너 클래스 앞에 static 키워드가 포함된 이너 클래스입니다.
정적 메서드와 동일하게 아우터 클래스의 정적 멤버만이 접근할 수 있으며, 이는 이너 클래스의 특성이 아닌 정적(static) 특성입니다.
즉, 아우터 클래스의 객체를 생성하지 않아도 정적 이너 클래스의 객체를 생성해 사용할 수 있어야 하므로 아우터 클래스의 멤버 중 객체 생성 없이 바로 사용할 수 있는 정적 멤버만 정적 이너 클래스 내부에서 사용할 수 있습니다.


- 정적 이너 클래스 객체 생성하기
컴파일 이후에는 인스턴스 멤버 클래스와 동일하게 `아우터 클래스.class`, `아우터 클래스$이너 클래스.class`의 바이트 코드 파일이 생성됩니다.
반면, 객체를 생성하는 방법은 아래와 같으며, 정적 이너 클래스도 말 그대로 정적 멤버이므로 클래스명으로 바로 접근할 수 있습니다.

```java
// 정적 멤버 이너 클래스의 객체 생성 방법
아우터 클래스.이너 클래스 이너 클래스 참조 변수 = new 아우터 클래스.이너 클래스();

// 예
class A {
    static class B {
        ...
    }
}

A.B b = new A.B();
```


### 지역 이너 클래스
지역 이너 클래스는 클래스의 멤버가 아닌, 메서드 내에서 정의되는 클래스입니다.
지역 변수처럼 정의된 메서드 내부에서만 사용할 수 있으므로 일반적으로 지역 이너 클래스는 선언 이후 바로 객체를 생성해 사용하며, 메서드가 호출될 때만 메모리에 로딩됩니다.
따라서 지역 이너 클래스는 정적 클래스로 지정할 수 없습니다.

지역 클래스를 컴파일하면 `아우터 클래스$+숫자+이너 클래스.class`와 같이 지역 이너 클래스 이름 앞에 숫자가 포함된 이름으로 클래스 파일이 생성됩니다.
이유는 지역 이너 클래스는 메서드 내에서만 정의하고 사용할 수 있으므로 여러 개의 메서드에서 동일한 이름의 지역 이너 클래스를 생성할 수도 있기 때문입니다.
동일한 지역 클래스명이 있을 때 숫자가 1부터 하나씩 증가합니다.


- 지역 이너 클래스 객체 생성하기
지역 이너 클래스도 다른 이너 클래스처럼 아우터 클래스의 멤버를 접근 지정자와 상관없이 사용할 수 있으며, 추가로 자신이 정의된 메서드의 지역 변수도 클래스 내부에서 사용할 수 있습니다.
다만, `지역 변수를 사용할 때는 반드시 해당 지역 변수가 final로 선언되어야 하며, 만일 final로 선언되지 않은 지역 변수를 지역 클래스 내부에서 사용할 때는 컴파일러가 강제로 해당 지역 변수에 final을 추가해 줍니다.`

```java
// 지역 이너 클래스의 객체 생성 방법
지역 이너 클래스 지역 이너 클래스 참조 변수 = new 지역 이너 클래스();

// 예
class A {
    void abc() {
        class B {
            ...         // 지역 이너 클래스
        }
        B b = new B();  // 지역 이너 클래스 객체 생성
    }
}
```


## 익명 이너 클래스

### 익명 이너 클래스의 정의와 특징
익명 이너 클래스는 정의된 위치에 따라 분류할 수 있으며, 클래스의 중괄호 바로 아래에 사용했을 때는 인스턴스 익명 이너 클래스, 메서드 내부에서 사용했을 때는 지역 익명 이너 클래스를 의미합니다.

> 정적 익명 이너 클래스는 객체 생성 없이 클래스명만으로 객체를 생성해야 하는데, 익명 이너 클래스는 이름을 알 수 없기 때문에 존재할 수 없습니다.

```java
// 인터페이스를 상속한 이너 클래스를 생성해 인터페이스 객체 생성
class A {
    C c = new B();
    void abc() {
        c.bcd();
    }
    class B implements C {
        public void bcd() {
            System.out.println("인스턴스 이너 클래스");
        }
    }
}
interface C {
    public abstrack void bcd();
}

public class AnonymousClass_1 {
    public static void main(String[] args) {
        A a = new A();
        a.abc();    // 인스턴스 이너 클래스
    }
}
```


```java
// 익명 이너 클래스를 활용해 인터페이스 객체 생성
class A {
    C c = new C() {
        public void bcd() {
            System.out.println("익명 이너 클래스");
        }
    };
    void abc() {
        c.bcd()
    }
}
interface C {
    public abstract void bcd();
}
public class AnonymousClass_2 {
    public static void main(String[] args) {
        A a = new A();
        a.abc();    // 익명 이너 클래스
    }
}
```

- 다음은 인터페이스 C를 상속받은 B 클래스에서 추가로 메서드를 정의했을 때 입니다.

```java
interface C {
    public abstrack void bcd();
}

// 객체를 생성
class B implements C {
    public void bcd() {
        // 메서드 구현
    }
    public void cde() {
        // 메서드 구현
    }
}

B b = new B();
b.bcd();    // (O)
b.cde();    // (O)


// 익명 클래스
C c = new C() {
    public void bcd() {
        // 메서드 구현
        // cde()    // 내부적으로 호출 가능
    }
    public void cde() {
        // 메서드 구현
    }
};

c.bcd();    // (O)
c.cde();    // (X)
```

자식 클래스 타입으로 객체를 선언하고 생성하면 오버라이딩된 메서드와 추가 메서드를 모두 사용할 수 있습니다.
반면, 익명 이너 클래스를 사용할 때는 `항상 부모 타입으로만 선언할 수 있으므로`추가로 정의한 메서드 cde()는 호출할 수 없습니다.

다만, 오버라이딩 메서드 내부에서는 호출할 수 있으므로 작성해야 할 내용이 많을 때 메서드를 분리해 작성하는 것이 효율적이며, 이때 익명 이너 클래스 정의식 내부에 추가 메서드를 정의해 사용하는 것이 편할 수 있습니다.


### 익명 이너 클래스를 활용한 인터페이스 타입의 입력매개변수 전달
다음 예제에서는 인터페이스 A에는 추상 메서드 abc(), 클래스 C에는 인터페이스 A타입의 객체를 입력매개변수로 포함하고 있는 메서드 cde(A a)가 있습니다.

```java
interface A {
    public abstrack void abc();
}
class C {
    void cde(A a) {
        a.abc();
    }
}
```

인터페이스 A의 객체를 생성하고, 메서드의 입력매개변수로 전달하는 방법은 문법적으로 크게 4가지 형태로 분류할 수 있습니다.

- 인터페이스 A의 자식 클래스 B를 직접 정의할 때
```java
class B implements A {
    public void abc() {
        // ...
    }
}
```

자식 클래스를 직접 정의했으므로 자식 클래스의 생성자를 호출함으로써 객체는 얼마든지 생성할 수 있습니다.
이때 생성한 객체를 메서드 입력매개변수로 전달하는 방식에 따라 다음과 같이 다시 2가지 형태를 지닙니다.

```java
C c = new C();

// 방법 (1)
A a1 = new B();
c.cde(a1);
// 방법 (2)
c.cde(new B());
```

먼저 (1) 번 방법은 B() 생성자를 이용해 생성한 객체를 A 타입의 참조 변수에 저장하고, 입력매개변수로 참조 변수를 넘겨주는 방식입니다.
이때 객체 참조 변수(a1)의 역할은 객체의 참조값을 전달하기 위해서만 사용됩니다.
따라서, 단순히 객체의 참조값만을 전달할 목적이라면 굳이 참조 변수를 사용하지 않고 메서드 입력매개변수 위치에서 바로 `new B()`와 같이 객체를 생성하면 생성된 객체의 참조값이 메서드로 전달될 것이며, 이 방법이 (2)입니다.

- 이번에는 자식 클래스를 별도로 정의하지 않고, 익명 이너 클래스를 사용해 메서드 입력매개변수로 객체를 전달하는 방법을 알아보겠습니다.

```java
C c = new C();

// 방법 (3)
A a = new A() {
    public void abc() {
        // ...
    }
};
c.cde(a);


// 방법 (4)
c.cde(new A() {
    public void abc() {
        // ...
    }
});
```

익명 이너 클래스 문법을 활용했다는 점을 제외하면 방법 (1), (2)와 같습니다.

여기서 방법 (3)은 익명 이너 클래스를 사용해 객체를 생성하고, 객체를 참조하는 참조 변수(a)를 cde() 메서드의 입력매개변수로 전달했습니다.

반면, 방법 (4)는 참조 변수를 대입하지 않고, 메서드 입력매개변수 자리에서 곧바로 익명 이너 클래스 객체를 생성해 전달하는 방식입니다.

4가지 방법 중 어떤 것을 사용해도 괜찮지만, 생성하는 객체의 개수, 객체의 사용 시점 등 상황에 따라 효율적인 방법이 다르므로 4가지 방법을 모두 알아두어야 합니다.
특히 마지막 방법은 이벤트 처리 등에 가장 많이 사용되는 형식이므로 꼭 기억해 두셔야 합니다.

```java
// 클래스 정의 및 참조 변수명을 사용/미사용했을 때 입력매개변수 객체 전달
interface A {
    public abstrack void abc();
}
// 자식 클래스 직접 생성
class B implements A {
    public void abc() {
        System.out.println("입력매개변수 전달");
    }
}
class C {
    void cde(A a) {
        a.abc();
    }
}
public class AnonymousClass_3 {
    public static void main(String[] args) {
        C c = new C();
        
        // 방법 1. 클래스명 O + 참조 변수명  O
        A a = new B();
        c.cde(a);

        // 방법 2. 클래스명 O + 참조 변수명 X
        c.cde(new B());
    }
}
```

```java
// 클래스 미정의 및 참조 변수명을 사용/미사용했을 때 입력매개변수 객체 전달
interface A {
    public abstrack void abc();
}
class C {
    void cde(A a) {
        a.abc();
    }
}
public class AnonymousClass_4 {
    public static void main(String[] args) {
        C c = new C();

        // 방법 3. 클래스명 X + 참조 변수명 O
        A a = new A() {
            public void abc() {
                System.out.println("입력매개변수 전달");
            }
        };
        c.cde(a);

        // 방법 4. 클래스명 X + 참조 변수명 X
        c.cde(new A() {
            public void abc() {
                System.out.println("입력매개변수 전달");
            }
        });
    }
}
```

앞에서 추상 클래스의 객체 생성 때도 언급했듯이 이 예제에서 볼 수 있는 바와 같이 익명 이너 클래스를 사용하면 직접 클래스를 추가로 정의해야 하는 수고로움을 덜 수도 있습니다.

다만, 여러 개의 객체를 생성하고자 할 때는 객체를 생성할 때마다 추상 메서드를 구현해야 하므로 이때는 익명 이너 클래스보다 직접 클래스를 추가로 작성하는 것이 좋습니다.


## 이너 인터페이스
이제 마지막으로 `이너 인터페이스(inner interface)`를 알아보겠습니다.

이너 클래스와 마찬가지로 인터페이스를 클래스 내부에 정의하는 것은 해당 클래스에 의존적인 기능을 수행할 때입니다.
예를 들어 버튼 클릭을 감지하는 인터페이스는 버튼 클래스 내부에 위치시키는 것이 바람직할 것입니다.

이러한 이유로 이너 인터페이스는 `사용자 인터페이스(user interface)`의 이벤트 처리에 가장 많이 사용됩니다.

> 일반적으로 사용자 인터페이스에서 이벤트를 감지하는 인터페이스를 `리스너`라고 합니다.


### 이너 인터페이스의 정의와 특징
이너 인터페이스의 중요한 특징 중 하나는 `정적 이너 인터페이스만 존재`할 수 있다는 것입니다.
이너 인터페이스 앞에 static 제어자를 생략하면 컴파일러가 자동으로 추가해 줍니다.

```java
class A {
    // ...
    static interface B {
        void bcd();
    }
}
```

컴파일하면 이너 클래스와 같이 `아우터 클래스명$이너 인터페이스명.class`형태로 바이트 코드인 .class 파일이 생성됩니다.

이너 인터페이스도 인터페이스이므로 자체적으로는 객체를 생성할 수 없습니다.
따라서 객체를 생성하기 위해서는 해당 인터페이스를 상속한 자식 클래스를 생성한 후 생성자를 이용해 객체를 생성하거나 익명 이너 클래스를 활용해 객체를 생성해야 합니다.

즉, 일반적인 인터페이스 객체를 생성하는 방법과 동일하며, 유일한 차이점은 인터페이스가 클래스 내부에 존재하므로 객체의 타입을 `아우터 클래스명.이너 인터페이스명`과 같이 사용해야 한다는 것입니다.

```java
// 방법 1. 인터페이스 구현 클래스 생성 및 객체 생성
class C implements A.B {
    public void bcd() {}
}

C c = new C();
c.bcd();


// 방법 2. 익명 이너 클래스 사용
A.B a = new A.B {
    public void bcd() {}
};
a.bcd();
```


```java
// 이너 인터페이스의 2가지 객체 생성 방법
class A {
    interface B {   // 컴파일러가 자동으로 static 지정
        public abstrack void bcd();
    }
}
class C implements A.B {
    public void bcd() {
        System.out.println("이너 인터페이스 구현 클래스 생성");
    }
}
public class InnerInterface {
    public static void main(String[] args) {
        // 객체 생성 방법 1(자식 클래스 직접 생성)
        A.B ab = new C();
        C c = new C();
        c.bcd();

        // 객체 생성 방법 2(익명 이너 클래스 생성)
        A.B b = new A.B() {
            public void bcd() {
                System.out.println("익명 이너 클래스로 객체 생성");
            }
        };
        b.bcd();
    }
}
```


### 이벤트 처리 기능 작성하기
사용자 인터페이스에서 사용되는 일반적인 이벤트 처리 기능을 이너 인터페이스를 이용해 작성해 보겠습니다.

먼저 Button 등과 같은 기본적인 사용자 인터페이스 클래스는 API로 제공됩니다.

기본적인 구조는 아래와 같습니다.

```java
class Button {
    onClickListener ocl;
    void setOnClickListener(OnClickListener ocl) {
        this.ocl = ocl;
    }
    interface OnClickListener {
        public abstrack void onClick();
    }
    void click() {
        ocl.onClick();
    }
}
```

- 내부에 `OnClickListener`라는 이너 인터페이스가 정의되어 있고, ocl 필드는 이 인터페이스의 타입입니다.

- `setOnClickListener()` 메서드는 이 인터페이스 객체를 입력매개변수로 넘겨받아 필드를 초기화하는 기능을 수행합니다.

- `click()` 메서드는 초기화된 필드 객체 내부의 `onClick()` 메서드를 실행시킵니다.

즉, Button은 기능은 내부에서 정해지는 것이 아니라 외부에서 정해 입력받는 것입니다.
이제 이렇게 API에서 제공받은 Button 클래스를 사용해 개발자가 Button에 기능을 부여하는 경우를 살펴보겠습니다.

```java
// 개발자 (1): 클릭하면 음악 재성
public static void main(String[] args) {
    Button button1 = new Button();
    button1.setOnClickListener(new Button.OnClickListener() {
        @Override
        public void onClick() {
            System.out.println("개발자 1. 음악 재생");
        }
    });
    button1.click();
}


// 개발자 (2): 클릭하면 네이버 접속
public static void main(String[] args) {
    Button button2 = new Button();
    button2.setOnClickListener(new Button.OnClickListener() {
        @Override
        public void onClick() {
            System.out.println("개발자 2. 네이버 접속");
        }
    });
    button2.click();
}
```

- 먼저 개발자 (1)은 버튼을 클릭했을 때 음악을 재생하는 기능을 구현하기 위해 버튼 객체를 생성했습니다.

- 이후 익명 이너 클래스를 활용해 onClick() 메서드를 오버라이딩 했습니다.

- 이렇게 생성한 객체를 setOnClickListener() 메서드의 입력매개변수로 전달한 후 Button 객체의 click() 메서드를 호출했습니다.

- 여기서 개발자 (2)는 버튼을 클릭했을 때 출력되는 것을 제외하면 개발자 (1)과 같습니다.


즉, API는 음악을 재생하는 버튼과 네이버를 접속하는 버튼을 따로 만들어 제공하는 것이 아니라 버튼의 기능을 정의할 수 있는 인터페이스를 클래스 내부에 정의해 제공합니다.
그러면 이 버튼을 사용하는 개발자가 이 인터페이스를 구현함으로써 버튼의 기능을 정의할 수 있는 것입니다.

즉, 1개의 버튼 클래스로 수천 개의 기능을 수행하는 버튼을 만들 수 있는 것입니다.
안드로이드를 포함해 일반적인 사용자 인터페이스 API는 이러한 구조를 뜁니다.


```java
// 일반적인 UI API의 구조 예시(버튼)
class Button {
    onClickListener ocl;
    void setOnClickListener(OnClickListener ocl) {
        this.ocl = ocl;
    }
    interface OnClickListener {
        public abstrack void onClick();
    }
    void onClick() {
        ocl.onClick();
    }
}

public class ButtonAPIExample {
    public static void main(String[] args) {
        // 개발자 (1): 클릭하면 음악 재생
        Button btn1 = new Button();
        btn1.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick() {
                System.out.println("개발자 1. 음악 재생");
            }
        });
        btn1.onClick();

        // 개발자 (2): 클릭하면 네이버 접속
        Button btn2 = new Button();
        btn2.setOnClickListener(new Button.OnClickListener() {
            @Override
            public void onClick() {
                System.out.println("개발자 2. 네이버 접속");
            }
        });
        btn2.onClick();
    }
}
```
