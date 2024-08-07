# 참조 자료형

## 배열
자바에서는 8개의 기본 자료형 이외의 모든 자료형은 참조 자료형입니다.
대표적인 참조 자료형은 `배열(array)`, `클래스(class)`, `인터페이스(interface)`등이 있습니다.

### 배열이란?
동일한 자료형을 묶어 저장하는 참조 자료형입니다.
생성할 때 크기를 지정해줘야 하고, 한 번 지정된 크기는 절대 변경할 수 없는 특징이 있습니다.

### 배열 생성하기
1. 배열 선언하기 : 
배열을 선언할 때는 다음과 같이 2가지 방법으로 선언할 수 있습니다.

- 1차원 배열의 선언 방법

| 자료형[] 변수명                  	| 자료형 변수명[]                  	|
|----------------------------------	|----------------------------------	|
| int[] a; double[] b; String[] c; 	| int a[]; double b[]; String c[]; 	|

> 다른 자료형과 다르게 array a 등으로 구현하지 않은 이유는 배열은 동일한 자료형만 묶을 수 있는 자료형이기 때문입니다.
따라서, array로 자료형을 주게 될 경우 어떤 자료형의 배열인지 인지하기 어렵기 때문에 위와같이 선언합니다.

배열을 선언하면 스택(stack) 메모리에 변수의 공간만 생성하고, 공간 안은 아직 배열의 실제 데이터인 객체를 생성하지 않았기 때문에 비운채로 둡니다.
스택 메모리에 위치하고 있는 참조 자료형 변수의 빈 공간을 초기화할 때는 null(널) 값을 사용할 수 있습니다.
여기서 null 값은 힙(heap) 메모리의 위치(address)를 가리키고 있지 않았다는 의미로 실제 데이터가 없다는 것을 의미합니다.

2. 힙 메모리에 배열의 객체 생성하기

참조 자료형의 실제 데이터는 힙 메모리에 생성되는데, 이를 생성하기 위해서는 `new` 키워드를 사용해야 합니다.

- 배열의 객체 생성

| new 자료형[배열의 길이]    	|
|----------------------------	|
| new int[3]; new String[5]; 	|

> 여기서 주의해야할 점은 배열의 길이를 지정하지 않고 `new int[]`와 같이 선언하면 오류가 발생되기 때문에 꼭 길이를 지정해줘야 합니다.

3. 배열 자료형 변수에 객체 대입하기 : 
선언된 배열 참조 자료형 변수에 생성한 객체를 대입하는 데는 2가지 방법이 있습니다.

이는 기본 자료형의 선언과 동시에 초기값을 주는 방법과 동일합니다

`int[] a = new int[3]`이는 글로 풀어보면 `int 자료형 3개를 저장할 수 있는 공간을 힙 메모리에 넣어두고, 어디에 넣었는지 참조 변수 a에 저장하겠다` 입니다.

> 스택 메모리 공간은 값을 초기화하지 않으면 빈(null) 공간으로 존재한다는 것이며, 당연히 이를 출력하게 되면 오류가 발생됩니다.
반면 힙 메모리는 어떤 상황에서도 빈 공간이 존재하지 않기 때문에 값을 주지 않으면 컴파일러가 강제로 값을 줍니다.

| 기본/참조 	| 자료형                            	| 기본값 	|
|-----------	|-----------------------------------	|--------	|
| 기본      	| 불리언(boolean)                   	| false  	|
|           	| 정수(byte, short/char, int, long) 	| 0      	|
|           	| 실수(float, double)               	| 0.0    	|
| 참조      	| 클래스(class), 배열(array), …     	| null   	|

> 객체의 위치를 참조 변수에 저장하는 이유는, JVM은 new 키워드를 이용해 객체를 생성하게 되면 힙 메모리 내에 비어 있는 공간에 객체를 생성하게 됩니다. 다만 여기서 객체의 위치를 참조하지 않고, 매번 비어 있는 공간이 다르게 되면 객체를 원할 때 사용할 수 없기 때문입니다.

4. 객체의 값 입력하기
생성한 객체에 값을 입력하기 위해서는 인덱스(index)를 활용하여 각 공간에 값을 넣어 줄 수 있습니다.
```Java
int[] a = new int[3];

a[0] = 3;
a[1] = 4;
a[2] = 5;

System.out.println(a[0]);
System.out.println(a[1]);
System.out.println(a[2]);
```

output
```
3
4
5
```

- 배열의 저장 공간에 값을 대입하거나 읽을 때, 없는 인덱스를 사용하게 되면 예외(exception)가 발생하고 프로그램이 종료됩니다.

### 1차원 배열을 생성하는 다양한 방법
위 방법 외에도 1차원 배열을 생성하는데 2가지 방법이 더 있습니다.

- 배열 객체 생성과 함께 값 대입하기
`자료형[] 참조 변수명 = new 자료형[] {값, 값2, ..., 값};` 이처럼 값을 그대로 넣어줄 수 있기 때문에 컴파일러의 강제 초기값은 생략되고, 길이 또한 중괄호 안에 값의 개수로 결정됩니다.

- 대입할 값만 입력하기
`자료형[] 참조 변수명 = {값, 값2, ..., 값};`으로 new 키워드 없이 값만 중괄호 안에 대입하는 방법입니다.

> 두 방법의 차이점은 대입의 분리 여부에 따라 다릅니다.
```Java
// 배열객체 생성과 함께 값 대입하기
int[] a = new int[]{3, 4, 5};   // O
int[] a;
a = new int[]{3, 4, 5};         // O

// 대입할 값만 입력하기
int[] a = {3, 4, 5};            // O
int[] a;
a = {3, 4, 5};                  // X
```


### 참조 자료형으로서 배열의 특징
기본 자료형은 스택 메모리에 실제 데이터값을 저장하고 있기 때문에 기본 자료형을 복사하면 실제로 데이터 값이 1개 더 복사가 되어, 복사된 값을 변경해도 원본 값은 영향이 가지 않습니다.
다만, 참조 자료형의 경우 힙 메모리에 저장된 값의 주소를 스택 메모리에 저장하고 있기 때문에, 참조 자료형을 복사하게 되면 값이 아닌 위치값이 복사되어 복사된 값을 변경하면 원본 값도 변경됩니다.

### 반복문을 이용해 배열 데이터 읽기
배열은 동일한 자료형으로 여러개 묶어 저장합니다.  때문에 값을 호출할 때 반복문을 사용할 수 있으며, 배열에 길이만큼 사용하기 위해서 `배열 참조 변수.length`를 사용합니다.
여기서 포인트 연산자(.)는 `해당 참조 변수가 가리키는 곳으로 가라`는 의미입니다.

- for-each 문을 사용하는 방법 : 
배열이나 컬렉션(collection)등의 집합 객체에서 원소들을 하나씩 커내는 과정을 반복하는 구문으로 집합 객체의 원소들을 출력할 때 사용합니다.

```Java
// for-each 문
for (원소 자료형 변수명: 집합 객체) {
    ...
}

// 예
int[] a = new int[100];
for (int i = 0; i < a.length; i++) {
    a[i] = i;
}

for (int k: a) {
    System.out.println(k);
}
```

- Arrays 클래스의 toString() 정적 메서드
```Java
package array.example_readArrayDate;

import java.util.Arrays;

public class ReadArrayData {
    public static void main(String[] args) {
        int[] array = new int[] {3, 4, 5, 6, 7};

        System.out.println(Arrays.toString(array));
    }
}
```

output
```
[3, 4, 5, 6, 7]
```

### 2차원 정방 행렬 배열
가로 및 세로 방향의 2차원으로 데이터를 저장하는 배열이 2차원 배열이고 그중 직사각형의 형태(모든 행의 길이가 같은 배열)를 띤 배열을 `2차원 정방 행렬 배열`이라고 합니다.

- 2차원 배열의 선언 방법

| 자료형[][] 변수명                      	| 자료형 변수명[][]                      	| 자료형[] 변수명[]                      	|
|----------------------------------------	|----------------------------------------	|----------------------------------------	|
| int[][] a; double[][] b; String[][] c; 	| int a[][]; double b[][]; String c[][]; 	| int[] a[]; double[] b[]; String[] c[]; 	|

> 2차원 정방 행렬은 객체를 생성하는 방법만 4가지가 있습니다.
하지만, 각 방법을 이해하는 것보다 더욱 중요한 사실은 `메모리는 2차원 데이터를 바로 저장할 수 없다.`는 것입니다.
즉 각각의 행이 1차원 배열이므로 `2차원 배열은 1차원 배열을 원소로 포함하고 있는 1차원 배열`입니다.

방법은 간단하게 1. 배열 객체를 생성한 뒤에 값을 대입하는 방법과 2. 배열 객체의 행 성분부터 생성하고 열 성분 생성하는 방법, 3. 배열의 자료형과 함께 대입할 값 입력하는 방법, 4. 대입할 값만 입력하는 방법이 있습니다.

> 3, 4번 방법의 경우 대괄호 처럼 옆으로 나열하는 것이 아닌, 중첩을 해줘야 합니다.


### 2차원 비정방 행렬 배열
각 행마다 열의 길이가 다른 2차원 배열을 의미하며, 2차원 정방 행렬 배열과 기본적인 개념은 동일합니다.
차이점은 1차원 배열을 원소로 포함하고 있는 1차원 배열들의 길이가 다양하다는 것입니다.

때문에, 생성 방법은 정방 행렬 배열과 동일하지만,위 4가지 방법 중 (1.)은 행렬을 미리 공통되게 생성하기 때문에 사용할 수 없습니다.

### 2차원 배열의 출력
2차원 배열은 행렬 방향으로 데이터가 분포돼 있어, 2가지의 인덱스를 사용하여 출력해야 합니다.  따라서, 이중 반복문을 사용해야 됩니다.

```Java
int[][] a = {{1, 2}, {3, 4, 5}};

// 이중 for 문을 이용한 2차원 배열 원소 출력
for (int i = 0; i < a.length; i++) {
    for (int j = 0; j < a[i].length; j++) {
        system.out.println(a[i][j]);
    }
}

// 이중 for-each 문을 이용한 2차원 배열 원소 출력
for (int[] m: a) {
    for (int[] n: m) {
        System.out.println(n);
    }
}
```

### main() 메서드의 입력매개변수
자바 코드를 실행하면 JVM에서 가장 먼저 실행하는 main() 메서드를 다시 한번 보면 입력 매개변수값의 눈이 갑니다.
`public static void main(String[] args) {}`다시 해석해 보면 main() 메서드의 입력 매개변수값으로 배열 변수명 args를 넘겨준다는 것을 알 수 있습니다.

> 콘솔을 이용하는 방법과 자바의 대표 IDE 중 하나인 이클립스를 이용하는 방법이 있습니다.
[Run -> Run Configurations] -> [Java Application 내에서 프로젝트명을 선택한 뒤에 [(x)=Arguments] 탭에서 입력한 매개변수값]이 전달됩니다. 


## 문자열을 저장하는 String
참조 자료형의 가장 대표적인 형태는 `클래스(class)`입니다.
이번에는 자바가 제공하는 클래스 중 문자열을 저장하는 String에 대해서 알아보겠습니다.

### 문자열의 표현과 객체 생성
String 클래스의 객체 생성 방법은 크게 2가지 입니다.

1. `String 참조 변수명 = new String("문자열");`

2. `String 참조 변수명 = "문자열";`

> 위 두 방식은 생성하는 방식은 달라도 메모리에 저장되는 방식은 동일합니다.

### String 클래스의 2가지 특징
String 클래스도 당연히 클래스이므로 다른 클래스들의 특징을 모두 지니고 있습니다.
하지만 자주 사용되는 클래스인 만큼 다른 클래스에는 없는 2개의 특징이 있습니다.

1. 한 번 정의된 문자열은 변경할 수 없습니다.
만일 문자열의 내용을 변경하면 JVM은 기존의 문자열을 수정하는 것이 아니라 새로운 문자열을 포함하고 있는 객체를 생성해 사용하고 기존 객체는 버립니다.

```Java
String str1 = new String("안녕");
String str2 = str1;
str1 = "안녕하세요";
System.out.println(str1);   // 안녕하세요
System.out.println(str2);   // 안녕
```

> 이는 참조 자료형에서 2개의 참조 변수가 1개의 객체를 가리킬 때 하나의 참조 변수에 접근해 객체의 값을 변경하면, 기존 값도 함께 변경되는 것과는 구분되는 특징입니다.

2. 문자열 리터럴을 바로 입력해 객체를 생성할 때 같은 문자열끼리 객체를 공유합니다.
문자열 리터럴만 입력해 String 객체를 생성하면 하나의 문자열을 여러 객체가 공유할 수 있습니다.
이는 다른 클래스에 없는 특징으로 특정 문자열의 객체를 여러 개 만들어 사용할 때 메모리 효율성을 증가시키기 위한 것입니다.

```Java
String str1 = new String("안녕");
String str2 = "안녕";
String str3 = "안녕";
String str4 = new String("안녕");
```

> new 키워드로 생성하게 되면 힙 메모리에 동일한 문자열 객체 유무 상관없이 새롭게 객체를 생성하게 되고, 문자열 리터럴로 생성할 때는 힙 메모리에 리터럴로 생성된 동일 문자열을 포함하고 있는 객체가 있으면 그 객체를 공유합니다.


### String 객체의 '+' 연산
+ 연산은 값을 더하는 의미와 연결하는 의미가 있고, 문자/문자열은 연결하는 의미로 사용됩니다.

> 하지만 위에서 알 수 있듯이 문자열은 변경이 되지 않기 때문에 각 연산값 만큼 메모리를 차지하게 됩니다.

### String 클래스의 주요 메서드
String 클래스는 문자열의 길이, 문자열 검색, 문자열 변환 및 연결 등 매우 풍부한 메서드를 제공합니다.

| 구분                	| 리턴 타입 	| 메서드                                                                                                                                         	| 설명                                                                                                            	|
|---------------------	|-----------	|------------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------	|
| 문자열 길이         	| int       	| length()                                                                                                                                       	| 문자열의 길이                                                                                                   	|
| 문자열 검색         	| char      	| charAt(int index)                                                                                                                              	| 인덱스 위치에서의 문자                                                                                          	|
|                     	| int       	| indexOf(int ch) indexOf(int ch, int fromIndex) indexOf(String str) indexOf(String str, int fromIndex)                                          	| 문자열에 포함된 문자 또는 문자열의 위치를 앞에서부터 검색했을 때 일치하는 인덱스 값(fromIndex는 검색 시작 위치) 	|
|                     	| int       	| lastIndexOf(int ch) lastIndexOf(int ch, int fromIndex) lastIndexOf(String str) lastIndexOf(String str, int fromIndex)                          	| 문자열에 포함된 문자 또는 문자열의 위치를 뒤에서부터 검색했을 때 일치하는 인덱스값(fromIndex는 검색 시작 위치)  	|
| 문자열 변환 및 검색 	| float     	| String.valueOf(boolean b) String.valueOf(char c) String.valueOf(int i) String.valueOf(long l) String.valueOf(float f) String.valueOf(double d) 	| boolean, char,  int, long,  float, double 값을 문자열로 변환하기 위한 정적 메서드                               	|
|                     	| double    	| concat(STring str)                                                                                                                             	| 문자열 연결(String 객체의 + 연산과 동일)                                                                        	|
| 문자열 배열 변환    	| byte[]    	| getBytes() getBytes(Charset charset)                                                                                                           	| 문자열을 byte[]로 변환(변환할 때 문자 셋(charset)지정 가능)                                                     	|
|                     	| char[]    	| toCharArray()                                                                                                                                  	| 문자열을 char[]로 변환                                                                                          	|

가장 대표적인 것만 추렸으며 아래와 같이 간략하게 알아보겠습니다.
- `length()`: 문자열의 길이를 리턴합니다.
- `charAt()`: 문자열에서 특정 인덱스에 위치해 있는 문자를 알아 냅니다.
- `indexOf()`: 문자열에서 특정 문자나 특정 문자열을 앞에서부터 찾아 위칫값을 알아냅니다.
- `lastIndexOf()`: 문자열에서 특정 문자나 특정 문자열을 뒤에서부터 찾아 위칫값을 알아냅니다.
- `String.valueOf()`: 기본 자료형을 문자열로 바꾸는 정적 메서드입니다.
- `concat()`: 2개의 문자열을 연결합니다. + 연산자와 동일한 기능을 수행합니다.
- `getBytes()`: 문자열을 byte 배열로 변환합니다. 자바 입출력 과정에서 주로 사용합니다.
- `toCharArray()`: 문자열을 char 배열로 변환합니다. 자바 입출력 과정에서 주로 사용합니다.


| 구분             	| 리턴 타입 	| 메서드                                                            	| 설명                                                                                                                           	|
|------------------	|-----------	|-------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------	|
| 문자열 수정      	| String    	| toLowerCase()                                                     	| 영문 문자를 모두 소문자로 변환                                                                                                 	|
|                  	| String    	| toUpperCase()                                                     	| 영문 문자를 모두 대문자로 변환                                                                                                 	|
|                  	| String    	| replace()char oldChar, char newChar)                              	| oldChar 문자열을 newChar 문자열로 대체한 문자열 생성                                                                           	|
|                  	| String    	| substring(int beginIndex) substring(int beginIndex, int endIndex) 	| beginIndex부터 끝까지의 문자열 생성 BeginIndex부터 endIndex - 1 위치까지의 문자열 생성                                         	|
|                  	| String[]  	| split(String regex) split(String regex, int limit)                	| regex를 기준으로 문자열을 분할한 문자열 배열을 생성(regex 구분 기호는 ‘\|’ 기호로 여러 개 사용 가능, limit는 분할의 최대 개수) 	|
|                  	| String    	| trim()                                                            	| 문자열의 앞뒤 공백 제거                                                                                                        	|
| 문자열 내용 비교 	| boolean   	| equals()                                                          	| 문자열의 실제 내용 비교 (==는 메모리 번지(stack) 비교)                                                                         	|
|                  	| boolean   	| equalsIgnoreCase(String anotherString)                            	| 대소문자 구분 없이 문자열의 실제 내용 비교                                                                                     	|

위 표도 간략하게 설명하면 아래와 같습니다.
- `toLowerCase()`: 영문 문자를 모두 소문자로 변환합니다.
- `toUpperCase()`: 영문 문자를 모두 대문자로 변환합니다.
- `replace()`: 일부 문자열을 다른 문자열로 대체합니다.
- `substring()`: 문자열의 일부만을 포함하는 새로운 문자열 객체를 생성합니다.
- `split()`: 특정 기호를 기준으로 문자열을 분리합니다.
- `trim()`: 문자열의 좌우 공백을 제거합니다.
- `equals()`: 두 문자열의 위치값이 아닌 실제 데이터값을 비교합니다. 이 떄 대소문자를 구분합니다.
- `equalsIgnoreCase()`: 두 문자열의 위칫값이 아닌 실제 데이터값을 비교합니다. 이 때 대소문자를 구분하지 않습니다.


```Java
package string MethodOfString;

public class MethodOfString {
    public static void main(String[] args) {
        String str1 = new String("Java");
        String str2 = new String("Java");
        String str3 = new String("java");

        System.out.println(str1.equals(str2));               // true
        System.out.println(str2.equals(str3));               // false
        System.out.println(str2.equalsIgnoreCase(str3));     // true
    }
}
```
