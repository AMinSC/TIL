# 제네릭

제네릭 클래스와 제네릭 메서드를 이해하면 자바에서 제공하는 다양한 종류의 클래스와 인터페이스를 좀 더 효율적으로 활용할 수 있습니다.

## 제네릭 클래스와 제네릭 인터페이스
내부 멤버에서 활용하는 클래스를 작성하고자 할 때는 제공되는 클래스나 인터페이스의 다양성 만큼이나 많은 가짓수의 클래스를 생성해야합니다.  또한 동일한 이름의 메서드가 다양한 타입의 입력매개변수를 가질 수 있도록 하려면 고려하는 입력매개변수 타입의 수만큼 오버로딩을 구현해야합니다.

이러한 비효율성을 한 번에 해결하는 데 필요한 문법 요소가 바로 `제네릭(generic)`입니다.

### 제네릭 없이 여러 객체를 저장하는 클래스 작성하기
Apple 클래스와 Pencil클래스를 담을 수 있는 Socket클래스를 예로 들어보겠습니다.

```java
// Package

// Apple 클래스와 Apple 클래스를 담을 수 있는 Socket01 클래스
class Apple {}
class Socket01 {
    private Apple apple = new Apple();
    public Apple getApple() {
        return apple;
    }
    public void setApple(Apple apple) {
        this.apple = apple;
    }
}

// Pencil 클래스와 Pencil 클래스를 담을 수 있는 Socket02 클래스
class Pencil {}
class Socket02 {
    private Pencil pencil = new Pencil();
    public Pencil getPencil() {
        return pencil;
    }
    public void SetPencil(Pencil pencil) {
        this.pencil = pencil;
    }
}

public class ProblemsBeforeGeneric {
    public static void main(String[] args) {
        // Socket01을 이용해 Apple 객체를 추가하거나 가져오기
        Socket01 socket01 = new Socket01();
        socket01.setApple(new Aplle());
        Apple apple = socket01.getApple();

        // Socket02를 이용해 Pencil 객체를 추가하거나 가져오기
        Socket02 socket02 = new Socket02();
        socket02.setPencil(new Pencil());
        Pencil pencil = socket02.getPencil();
    }
}
```

사과와 연필을 관리하기 위해 각각의 기능을 수행하는 클래스를 2개 만든것을 확인 할 수 있습니다.

따라서 새로운 상품이 추가된다면 기능을 수행하는 클래스를 추가해야되는 번거로움이 발생됩니다.  이를 해결하기 위한 방법이 없을지 생각해볼 수 있고, 첫 번째로 최상위 클래스인 Object 타입을 선언해보는 방법이 있습니다.

```java
// Package

// Apple, Pencil 클래스를 모두 저장하거나 꺼낼 수 있는 클래스 (Object 클래스 활용)

class Apple {}
class Pencil {}

class Socket {
    private Object object = new Object();
    public Object getObject() {
        return object;
    }
    public void setObject(Object object) {
        this.object = object;
    }
}

public class Solution_UsingObject {
    public static void main(String[] args) {
        // Socket을 이용해 Apple 객체를 추가하거나 가져오기
        Socket socket01 = new Socket();
        socket01.setObject(new Apple());
        Apple apple = (Apple)socket01.getObject();

        // Socket을 이용해 Pencil 객체를 추가하거나 가져오기
        Socket socket02 = new Socket();
        socket02.setObject(new Pencil());
        Pencil pencil = (Pencil)socket02.getObject();

        // 잘못된 캐스팅(약한 타입 체크)
        // Socket socket03 = new Socket();
        // socket03.setObject(new Apple());
        // Pencil pencil02 = (Pencil)socket03.getObject();  // 예외 발생
    }
}
```

> 우선 잘못된 캐스팅했을 때 발생하는 예외인 ClassCastException은 실행 예외이기 때문에 문법오류는 발생되지 않습니다.
하지만 이러한 잘못된 캐스팅은 실행 중 예외를 발생시키고, 프로그램은 강제로 종료될 것입니다.
이를 `약한 체크 타입(Weak Type Checking)`라고 합니다.

지금까지의 내용을 정리해보자면, 각 상품마다 각각의 클래스를 생성하는 대신, 최상위 클래스인 Object 타입의 필드를 선언하면 모든 타입의 상품을 저장할 수 있는 클래스를 생성할 수 있지만, get() 메서드의 경우 명시적인 다운 캐스팅이 필요하고 잘못된 캐스팅으로 예외가 발생될 수 있습니다.


## 제네릭의 문법

> 제네릭을 사용하면 다양한 클래스를 활용할 수 있으면서 잘못된 다운 캐스팅을 할 때 문법 오류를 발생시켜 문제를 사전에 예방할 수 있습니다.
이를 `강한 체크 타입(Strong Type Checking)`라고 합니다.

이를 이해하기 앞서 문법 구조를 알아보겠습니다.

### 제네릭 클래스와 제네릭 인터페이스 정의하기

제네릭의 문법 구조는 클래스와 인터페이스 뒤에 <제네릭 타입>을 적어 줍니다.

`Socket<T> or Sockets<K, V>`

제네릭 타입 변수명은 사용자가 임의로 지정할 수 있지만, 일반적으로 영문 대문자 한글자를 사용합니다.

- 관례적으로 사용하는 제네릭 타입 변수명
    | 제네릭 타입 변수 	| 의미          	|
    |------------------	|---------------	|
    | T                	| 타입(Type)    	|
    | K                	| 키(Key)       	|
    | V                	| 값(Value)     	|
    | N                	| 숫자(Number)  	|
    | E                	| 원소(Element) 	|


- 예시 제네릭 클래스
    ```java
    public class Myclass<T> {
        private T t;
        public T get() {
            return t;
        }
        public void set(T t) {
            this.t = t;
        }
    }
    ```


### 제네릭 클래스의 객체 생성

제네릭 클래스의 객체 생성 과정은 일반 클래스의 객체 생성과정과 크게 다를게 없습니다.
다만, 제네릭 클래스는 클래스를 정의하는 시점에 타입을 지정하는 것이 아닌, 객체를 생성하는 시점에 타입을 지정하기 때문에 `객체를 생성할 때 제네릭 타입 변수에 실제 타입을 대입해야 합니다.`

- 객체의 생성 과정에서 생성자명에 포함된 오른쪽 항의 실제 제네릭 타입은 항상 왼쪽 항과 동일하기 때문에 생략할 수 있습니다.

```java
//Package

class MyClass<T> {
    private T t;
    public T get() {
        return t;
    }
    public void set(T t) {
        this.t = t;
    }
}

public class SingleGenericArgument {
    public static void main(String[] args) {
        MyClass<String> mc01 = new MyClass<>();
        mc01.set("안녕");
        System.out.println(mc01.get());  // 안녕
        MyClass<Integer> mc02 = new MyClass<>();
        mc02.set(100);
        System.out.println(mc02.get());  // 100
    }
}
```

아래는 제네릭 타입 변수가 2개일 때의 예시 입니다.

```java
//Package

class MyClass<K, V> {
    private K k;
    private V v;
    public K getKey() {
        return k;
    }
    public void setKey(K k) {
        this.k = k;
    }
    public V getVal() {
        return v;
    }
    public void setVal(V v) {
        this.v = v;
    }
}

public class TwoGenericArgument {
    public static void main(String[] args) {
        MyClass<String, Integer> kv01 = new MyClass<>();
        kv01.setKey("사과");
        kv01.setVal(1000);
        String key01 = kv01.getKey();
        int val01 = kv01.getVal();
        System.out.println("key: " + key01 + " value: " + val01);  // key: 사과 value: 1000

        MyClass<String, void> kv02 = new MyClass<>();
        kv02.setKey("키 값만 사용");
        String key02 = kv02.getKey();
        System.out.println("key: " + key02);  // key: 키 값만 사용
    }
}
```

추가로 제네릭 클래스의 객체를 생성할 때 제네릭 타입을 생략해도 문법 오류는 발생하지 않습니다.
이유는 최상위 클래스인 Object가 대입된것으로 간주해 객체가 생성되기 때문입니다.

## 제네릭 메서드

클래스 전체를 제네릭으로 선언하는 대신, 일반 클래스 내부의 특정 메서드만 제네릭으로 선언할 수도 있으며, 이를 제네릭 메서드라고 합니다.

### 제네릭 메서드의 정의와 호출
제네릭 메서드를 정의할 때는 리턴 타입과 입력매개변수의 타입을 제네릭 타입 변수로 선언합니다.
제네릭 클래스가 객체를 생성하는 시점에 실제 타입을 지정하는 것과 달리 `제네릭 메서드는 호출되는 시점에 실제 제네릭 타입을 지정합니다.`

- 제네릭 메서드의 문법 구조
```java
// 제네릭 타입 변수명이 1개일 때
접근 지정자 <T> T 메서드명 (T t) {
    // 타입 T를 위한 기능 코드
}

// 제네릭 타입 변수명이 2개일 때
접근 지정자 <T, V> T 메서드명 (T t, V v) {
    // 타입 T, V를 위한 기능 코드
}

// 매개변수에만 제네릭이 사용됐을 때
접근 지정자 <T> void 메서드명 (T t) {
    // 타입 T를 위한 기능 코드
}

// 리턴 타입에만 제네릭이 사용됐을 때
접근 지정자 <T> T 메서드명 (int a) {
    // 타입 T를 위한 기능 코드
}
```

다음은 제네릭을 선언과 동시에 호출하는 코드입니다.

```java
// Package

// 일반 클래스 안에 제네릭 메서드
class GenericMethods {
    public <T> T method01(T t) {
        return t;
    }
    public <T> Boolean method02(T t1, T t2) {
        return t1.equals(t2);
    }
    public <K, V> void method03(K k, V v) {
        System.out.println(k + ":" + v);
    }
}

public class GenericMethod {
    public static void main(String[] args) {
        GenericMethods gm = new GenericMethods();

        String str1 = gm.<String>method01("안녕");  // 제네릭 타입을 String으로 지정
        String str2 = gm.method01("안녕");  // 입력매개변수값으로 제네릭 타입을 유추할 수 있을 때 제네릭 타입 지정 생략 가능
        
        boolean bool1 = gm.<double>method02(2.5, 2.5);
        boolean bool2 = gm.method02(2.5, 2.5);

        gm.<String, Integer>method03("국어", 80);
        gm.method03("국어", 80);
    }
}
```

제네릭 메서드를 호출할 때 2가지 방법을 적절하게 사용하면 된다.

### 제네릭 메서드 내에서 사용할 수 있는 메서드
제네릭 타입 변수는 메서드가 호출되는 시점에 결정됩니다.
따라서 제네릭 메서드를 정의하는 시점에서는 아직 어떤 타입이 입력될 것인지 전혀 알 수 없습니다.
때문에 특정 타입에 포함되어 있는 메서드(String 객체의 lenght() 등)는 메서드를 정의하는 시점에 사용할 수 없습니다.

그렇다고 이전처럼 Object 메서드만 사용한다면 활용 범위는 매우 좁아지고 전혀 유용하게 사용되지 않을 것입니다.
따라서 이를 해결하기 위해 제네릭 타입의 범위 제한을 알아보겠습니다.

## 네제릭 타입 범위 제한

### 제네릭 타입 범위 제한의 필요성
제네릭 타입의 경우 일반적으로 모든 타입이 적용 가능하지만, 예를 들어 문자열과 숫자 혹은 과일과 문구들의 클래스 타입별로 제한할 수 있다면 내부적으로 메서드사용도 가능할 것입니다.  이렇게 기능별로 구현하려면 제네릭 타입으로 올 수 있는 실제 타입의 종류를 제한하는 것을 `제네릭 타입의 범위 제한(bound)`라고 합니다.

따라서 과일 객체로 제한 한다면 사과, 배, 딸기 등과 같은 과일의 하위 클래스들이 올 수 있고, 문구 객체로 제한 한다면 연필, 볼펜, 지우개 등의 문구의 하위 클래스들을 사용할 수도 있습니다.

> Number 클래스는 8개의 기본 자료형 중 숫자를 저장하는 6개의 기본 자료형(byte, short, int, long, float, double)을 클래스로 포장(wrapping)한 클래스들(Byte, Short, Integer, Long, Float, Double)의 공통된 ㅌ늑성을 뽑아 정의한 부모 클래스입니다.


### 제네릭 타입 범위 제한의 종류와 타입 범위 제한 방법
제네릭 타입의 범위를 제한하는 방법은 아래 3가지 방식으로 나눠볼 수 있습니다.
- 제네릭 클래스에서 제네릭 타입을 제한할 때
- 제네릭 메서드에서 제네릭 타입을 제한할 때
- 일반 메서드의 매개변수로서 제네릭 클래스의 타입을 제한할 때

#### 제네릭 클래스의 타입 제한
예를 들어 `<T extends Fruit>`으로 작성한다면 Fruit 객체 또는 Fruit의 자식 클래스 객체만 대입할 수 있게 됩니다.

여기서 주의해야할 점은 extends키워드는 상속에서 사용한 것처럼 `상속하라`의 의미가 아니라 `최상위 클래스/인터페이스로 지정한다`의 의미를 갖는다는 것입니다.  따라서 상속에서와 달리, 뒤에 요소가 `클래스이든, 인터페이스이든 항상 extends 키워드를 사용해야 합니다.`

예를 들어 A <- B <- C 의 상속 구조를 가지고 있을때 제네릭 클래스 D로 아래와 같이 제한해보겠습니다.
```java
// Package

class A {}
class B extends A {}
class C extends B {}

class D <T extends B> {  // B와 C만 올 수 있음
    private T t;
    public T get() {
        return t;
    }
    public void set(T t) {
        this.t = t;
    }
}

public class BoundedTypeOfGenericClass {
    public static void main(String[] args) {
        // D<A> d1 = new D<>();  // 불가능
        D<B> d2 = new D<>();
        D<C> d3 = new D<>();
        D d4 = new D();  // D<B> d4 = new D<>();

        d2.set(new B());
        d2.set(new C());

        // d3.set(new B());  // d3 객체는 객체를 생성할 때 제네릭 타입으로 C를 지정하므로 B객체는 입력 불가능
        d3.set(new C());

        d4.set(new B());
        d4.set(new C());
    }
}
```

#### 제네릭 메서드의 타입 제한
제네릭 클래스와 동일하게 <제네릭 타입 변수 extends 상위 클래스>와 같이 올 수 있는 최상위 타입을 정의하며, 클래스와 인터페이스 모두 extends 키워드를 사용합니다. `즉, 제네릭 클래스일 때와 동일한 타입 제한 방식이 적용됩니다.`

제네릭 메서드에서 중요한 것은 메서드 내부에서 사용할 수 있는 메서드의 종류입니다. 타입을 제한하지 않을 경우 최상위 클래스인 Object 메서드만 사용할 수 있지만, `<T extends String>`과 같이 작성하게 되면 올 수 있는 모든 타입의 최상위 타입이 String이기 때문에 해당 제네릭 메서드의 내부에서는 String 객체의 멤버(필드/메서드)를 사용할 수 있습니다.

```java
class GenericMethods {
    // 불가능
    public <T> void method1(T t) {
        char c = t.charAt(0);  // Object 메서드만 사용 가능하기 때문에 불가
        System.out.println(c);
    }
    // 가능
    public <T extends String> void method2(T t) {
        char c = t.charAt(0);  // String 메서드 사용할 수 있기 때문에 가능
        System.out.println(c);
    }
}
```

아래는 추상 메서드를 포함한 인터페이스를 제네릭 메서드로 구현하는 방법입니다.
```java
// Package

class A {
    public <T extends Number> void method1(T t) {
        System.out.println(t.intValue());
    }
}

interface MyInterface {
    public abstract void print();
}

class B {
    public <T extends MyInterface> void method(T t) {
        t.print();
    }
}

public class BoundedTypeOfGenericMEthod {
    public static void main(String[] args) {
        A a = new A();
        a.method1(5.8);  //  = a.<Double>method1(5.8)

        B b = new B();
        b.method1(new MyInterface() {
            @Override
            public void print() {
                System.out.println("print() 구현");
            }
        });
    }
}
```
output
```
5
print() 구현
```

#### 메서드 매개변수일 때 제네릭 클래스의 타입 제한
입력매개변수에 입력되는 제네릭 클래스 객체의 제네릭 타입은 크게 4가지 형태로 제한할 수 있습니다.
```java
method(Socket<A> v)                 // 제네릭 타입 = A인 객체만 가능
method(Socket<?> v)                 // 제네릭 타입 = 모든 타입인 객체 가능
method(Socket<? exnteds B> v)       // 제네릭 타입 = B 또는 B의 자식 클래스인 객체만 가능
method(Socket<? super B> v)         // 제네릭 타입 = B 또는 B의 부모 클래스인 객체만 가능
```

제네릭 타입을 알 수 있는 자바 예시 코드는 아래와 같습니다.

```java
// Package

class A {}
class B extends A {}
class C extends B {}
class D extends C {}

class Socket<T> {
    private T t;
    public T get() {
        return t;
    }
    public void set(T t) {
        this.t = t;
    }
}

class Test {
    void method1(Socket<A> g) {}            // case1
    void method2(Socket<?> g) {}            // case2
    void method3(Socket<? extends B> g)     // case3
    void method4(SOcket<? super B> g)       // case4
}

public class BoundedTypeOfInputArguments {
    public static void main(String[] args) {
        Test t = new Test();

        // case1
        t.method1(new Socket<A>());
        // t.method1(new Socket<B>());
        // t.method1(new Socket<C>());
        // t.method1(new Socket<D>());

        // case2
        t.method2(new Socket<A>());
        t.method2(new Socket<B>());
        t.method2(new Socket<C>());
        t.method2(new Socket<D>());

        // case3
        // t.method3(new Socket<A>());
        t.method3(new Socket<B>());
        t.method3(new Socket<C>());
        t.method3(new Socket<D>());

        // case4
        t.method2(new Socket<A>());
        t.method2(new Socket<B>());
        // t.method2(new Socket<C>());
        // t.method2(new Socket<D>());
    }
}
```

## 제네릭의 상속
### 제네릭 클래스의 상속
부모 클래스가 제네릭 클래스일 경우, 이를 상속한 자식 클래스도 제네릭 클래스가 됩니다.
즉, 제네릭 타입 변수를 자식 클래스가 그대로 물려받게 됩니다.  또한 자식 클래스는 제네릭 타입 변수를 추가해 정의할 수도 있기 떄문에 자식 클래스의 제네릭 타입 변수의 개수는 항상 부모보다 같거나 많습니다.

```java
// 부모 클래스와 제네릭 타입 변수의 개수가 동일할 때
class Parent<K, V> {
    // ...
}
class Child<K, V> extends Parent<K, V> {
    // ...
}

// 부모 클래스보다 제네릭 타입 변수의 개수가 많을 때
class Parent<K> {
    // ...
}
class Child<K, V> extends Parent<K> {
    // ...
}
```

제네릭 클래스의 상속 예시 코드는 아래와 같습니다.
```java
// Package

clas Parent<T> {
    T t;
    public T getT() {
        return t;
    }
    public void setT(T t) {
        this.t = t;
    }
}

class Child1<T> extends Parent<T> {

}

class Child2<T, V> extends Parent<T> {
    V v;
    public V getV() {
        return v;
    }
    public void setV(V v) {
        this.v = v;
    }
}

public class IngeritanceGenericClass {
    public static void main(String[] args) {
        // 부모 제네릭 클래스
        Parent<String> p = new Parent<>();
        p.setT("부모 제네릭 클래스");
        System.out.println(p.getT());

        // 자식 제네릭 클래스 1
        Child1<String> c1 = new Child1<>();
        c1.setT("자식 1 제네릭 클래스");
        System.out.println(c1.getT());

        // 자식 제네릭 클래스 2
        Child2<String, Integer> c2 = new Child2<>();
        c2.setT("자식 2 제네릭 클래스");
        c2.setV(100);
        System.out.println(c2.getT());
        System.out.println(c2.getV());
    }
}
```
output
```
부모 제네릭 클래스
자식 1 제네릭 클래스
자식 2 제네릭 클래스
100
```

### 제네릭 메서드의 상속
제네릭 메서드를 포함한 일반 클래스를 상속해 자식 클래스를 생성할 때도 기존의 클래스 상속과 동일하게, 부모 클래스의 내의 제네릭 메서드도 그대로 자식 클래스로 상속됩니다.

아래 예제는 부모클래스로부터 최상위 제네릭 타입이 Number로 제한되어 있는 print() 제네릭 메서드를 상속받아 사용하는 예입니다.

> 참고로 이미 다룬 바와 같이 Number 클래스는 boolean과 char를 제외한 기본 자료형 6개의 `래퍼 클래스(wrapper class)`의 부모 클래스이고, 각 클래스의 이름은 Byte, Short, Integer, Long, Float, Double입니다.

```java
// Package

class Parent {
    <T extends Number> void print(T t) {
        System.out.println(t);
    }
}
class Child extends Parent {}

public class IngeritanceGenericMEthod {
    public static void main(String[] args) {

        // 부모 클래스에서 제네릭 메서드 이용
        Parent p = new Parent();
        p.<Integer>print(10);
        p.print(10);

        // 자식 클래스에서 제네릭 메서드 이용
        Child c = new Child();
        c.<Double>print(5.8);
        c.print(5.8);
    }
}
```
output
```
10
10
5.8
5.8
```

