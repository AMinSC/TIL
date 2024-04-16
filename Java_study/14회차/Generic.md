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

### 제네릭 타입 범위 제한의 종류와 타입 범위 제한 방법

## 제네릭의 상속
### 제네릭 클래스의 상속
### 제네릭 메서드의 상속
