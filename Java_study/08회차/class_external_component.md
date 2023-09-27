# 클래스 외부 구성 요소

## 패키지와 임포트

### 패키지
`패키지(package)는 비슷한 목적으로 생성된 클래스 파일들을 한 곳에 모아 둔 폴더`를 의미합니다.

프로그램을 작성하다 보면 각각의 목적에 따라 여러 개의 클래스 파일(네트워크 처리를 위한 클래스 10개, GUI 처리를 위한 클래스 8개 등)들이 생깁니다.  이렇게 동일한 목적으로 만들어진 클래스들을 1개의 공간(폴더)에 묶어 관리하기 위해 사용하는 것이 `패키지`입니다.

- 1개의 프로젝트에 1개의 패키지를 생성할 수도 있고, 여러 개의 패키지를 생성할 수도 있습니다.

- 또한 패키지를 아예 생성하지 않아도 문법적으로 전혀 문제가 없습니다.

> 자바 제공 API의 대표적인 패키지에는 기본 클래스들을 묶어 놓은 java.lang, 유용한 확장 클래스들을 묶어 놓은 java.util, 자바 그래픽과 관련된 클래스들을 묶어 놓은 java.swing과 javafx 그리고 자바의 입출력 클래스들을 묶어 놓은 java.io와 java.nio 패키지 등이 있습니다.

패키지를 생성하지 않으면 src 폴더 아래에 소스 파일이 바로 위치합니다.  `(default package)는 하위 폴더가 없음을 의미합니다.`

반면에 패키지를 지정하게 되면 지정된 패키지 폴더가 src폴더 아래에 생성되며, 그 아래에 소스 파일이 위치합니다.


```
package
├─JRE System Library [JavaSE-11]
└─src
   └─css
      ├─(default package)
      │   └─PackageTest1.java
      └─mypack.test
          └─PackageTest2.java
```

> 컴파일이 수행되면 바이트 코드가 저장되는 bin 폴더에도 동일한 하위 폴더가 생성됩니다.

```java
// 패키지를 생성하지 않았을 때
// package 구문 미포함

public class PackageTest1 {
    ...
}


// 패키지를 생성했을 때
package mypack.test;  // package 구문 포함

public class PackageTest2 {
    ...
}
```

- 패키지 사용의 장점 중 하나는 패키지의 영향으로 클래스가 저장되는 공간이 분리돼 클래스명의 충돌을 방지할 수 있다는 것입니다.

> 여기서 만약 패키지의 이름을 엔드포인트(.) 기준으로 앞은 동일하지만 뒤는 다르게 한다면(반대로 앞은 다르지만 뒤는 동일하게 한다면) 오류가 없는지 알아보자

### 임포트
다른 패키지 내의 클래스를 사용하기 위한 문법 요소로, 소스 코드상에서 패키지 구문의 다음 줄에 위치합니다.

프로그램이 동작할 때는 일반적으로 자신의 패키지 내부의 위치한 클래스만 사용할 수 있지만, 자바가 제공하는 API, 혹은 다른 사용자가 만든 패키지에 위치한 클래스를 사용하고자 할 때는 어떻게 해야 되는지 아래 2가지 방법으로 알아보겠습니다.

1. 클래스의 풀네임 사용
클래스의 풀네임은 `패키지명.클래스명`입니다.
따라서 `packageimport.common` 패키지의 A 클래스 객체를 생성하려면 단순 `A a = new A()`가 아닌, `packageimport.common.A a = new packageimport.A()`와 같이 사용해야 합니다.

```java
package packageimport.common;

public class A {
    public int m = 3;
    public int n = 4;
    public void print() {
        System.out.println("임포트");
    }
}
```

```java
package packageimport.ExamplePackageImport;

public class PackageImport {
    public static void main(String[] args) {
        packageimport.common.A a = new packageimport.common.A();
    }
}
```


2. 임포트 사용
(1.) 번 방법만 가지고 사용하게 되면 코드가 많이 지저분해 보이고 비효율적입니다.
하지만 임포트를 하게 되면 좀 더 간결하게 코드를 작성할 수 있습니다.
예를 들어 `import 패키지명.클래스명`을 기준으로 위 코드를 사용한다면 `import packageimport.common.A;`를 선언하고서 `A a = new A();`만으로 사용이 가능합니다.

```java
package packageimport.ExamplePackageImport_2;

import packageimport.common.A;

public class PckageImport_2 {
    A a = new a();
}
```

> 만일 패키지 내의 모든 클래스를 임포트 하고 싶다면 *를 사용하면 됩니다.
`import packageimport.common.*;`

- 실제 임포트되는 대상은 소스 코드(.java)가 아닌 bin 폴더에 위치한 컴파일이 완료된 바이트 코드(.class)입니다.
*기호를 사용할 때 주의해야 할 점은 `하위 폴더는 임포트 되지 않으며, 클래스 파일들만 임포트 된다는 것입니다.`

```
bin
└─pack1
   ├─pack2
   │  ├─C.class
   │  └─D.class
   ├─A.class
   └─B.class
```

```java
import pack1.*;
import pack1.pack2.*
```


## 외부 클래스
외부 클래스(external class)는 public 클래스의 외부에 추가로 정의한 클래스를 말합니다.

1개의 자바 소스 파일에는 최대 1개의 public 클래스만 존재할 수 있기 때문에 그 클래스명은 파일명과 일치해야 합니다.
즉, 1개의 소스 파일 안에서 public 클래스를 제외한 모든 클래스는 외부 클래스입니다.

public 클래스가 아니면 다른 패키지에서 임포트 할 수 없으므로 외부 클래스는 같은 패키지 안에서만 사용할 수 있습니다.

- 때문에 다른 패키지에서도 외부 클래스를 사용하려면 별도의 소스 파일로 작성한 후 public을 붙야 합니다.

- 소스 코드상에서 패키지, 임포트, 외부 클래스 순으로 순서를 지켜 위치해야 하며, 이들 3가지 요소 이외에는 어떤 문법 요소도 위치할 수 없다는 것을 꼭 알아둬야 합니다.
