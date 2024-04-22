# 컬렉션 프레임워크_04 (Stack, Queue)

## `Stack<E>` 컬렉션 클래스
### `Stack<E>` 컬렉션의 특징
`Stack<E>` 컬렉션은 5개의 컬렉션 중 유일하게 클래스입니다.
즉, 자체적으로 객체를 생성할 수 있습니다.

상속 구조를 살펴보면 `List<E>` 컬렉션의 구현 클래스인 `Vector<E>`클래스의 자식 클래스로 `후입선출(LIFO: Last In First Out)` 자료구조를 구현한 컬렉션입니다.

`LIFO는 말 그대로 나중에 입력된 데이터가 먼저 출력되는 것으 말합니다.`
당연히 `Vector<E>`의 모든 기능을 포함하고 있으며, 여기에 추가로 LIFO 구조를 위한 5개의 메서드가 추가됐습니다.

> 자바의 스택 메모리 영역도 데이터를 LIFO 방식으로 입출력합니다.

### `Stack<E>`의 주요 메서드
LIFO를 위해 추가된 5개의 메서드표는 아래와 같습니다.

| 구분             	| 리턴 타입 	| 메서드명         	| 기능                                                                  	|
|------------------	|-----------	|------------------	|-----------------------------------------------------------------------	|
| 데이터 추가      	| E         	| push(E item)     	| 매개변수의 item을 Stack<E>에 추가                                     	|
| 데이터 확인      	| E         	| peek()           	| 가장 상위에 있는 원소값 리턴(데이터의 변화는 없음)                    	|
| 데이터 위치 검색 	| int       	| search(Object o) 	| Stack 원소의 위치값을 리턴(맨 위의 값이1, 아래로 내려갈수록 1씩 증가) 	|
| 데이터 추출      	| E         	| pop()            	| 최상위 데이터 꺼내기(데이터의 개수 감소)                              	|
| empry 여부 검사  	| boolean   	| empty()          	| Stack<E> 객체가 비어 있는지 여부를 리턴                               	|

여기서 한 가지 주의해야 할 점은 앞에서 말한 것처럼 `Stack<E>`는 `Vector<E>`의 자식 클래스입니다.
즉, `Vector<E>`에 포함되어 있는 add() 메서드나 remove() 메서드로도 데이터의 추가 및 삭제를 수행할 수 있습니다만 `Vector<E>`의 메서드를 사용할 때는 LIFO의 특성이 반영되지 않습니다.
따라서 `Stack<E>` 본연의 특징을 갖기 위해서는 `Stack<E>`에서 추가한 5개의 메서드를 사용해야 합니다.

아래는 `Stack<E>` 클래스의 주요 메서드를 활용한 예시 코드입니다.

```java
// package
import java.util.Stack;

public class StackMethod {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        // 1. E push(E element)
        stack.push(2);
        stack.push(5);
        stack.push(3);
        stack.push(7);
        // 2. E peek()
        System.out.println(stack.peek());
        System.out.println(stack.size());
        System.out.println();
        // 3. search(Object o)
        System.out.println(stack.search(7));
        System.out.println(stack.search(3));
        System.out.println(stack.search(5));
        System.out.println(stack.search(2));
        System.out.println(stack.search(9));
        System.out.println();
        // 4. E pop()
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println();
        // 5. boolean empty()
        System.out.println(stack.empty());
    }
}
```
output
```
7
4

1
2
3
4
-1

7
3
5
2

true
```


## `Queue<E>` 컬렉션 인터페이스
### `Queue<E>` 컬렉션의 특징
`List<E>`와 `Set<E>`처럼 `Collection<E>`에게서 상속된 인터페이스로 앞에서 언급한 `LinkedList<E>`가 `Queue<E>` 인터페이스를 구현한 것입니다.

`Queue<E>`의 가장 큰 특징은 `Stack<E>`의 LIFO와 반대되는 개념은 `선입선출(FIFO: First In First Out)`구조를 가진다는 것입니다.
즉 먼저 저장된 데이터가 먼저 출력됩니다.

앞에서 다룬 여러 컬렉션 중에서 `Linked`가 붙은 컬렉션은 입력 순서 정보를 저장하기 때문에 입력 순서가 동일하다고 했습니다.
이것이 바로 `Queue<E>`의 특징이라고 생각하면 됩니다.

### `Queue<E>`의 주요 메서드
`Queue<E>` 내에 FIFO 기능을 부여하는 메서드는 2쌍이 존재합니다.
이 둘 사이의 유일한 차이점은 데이터가 없을 때 예외를 발생시키느냐, 기본값으로 대체하느냐입니다.

> 사실 기본값이라고 해 봐야 데이터가 없을 때 null을 리턴하는 것이 전부입니다.
하지만 적절한 예외 처리 없이 예외가 발생하면 프로그램이 강제 종료되기 때문에 예외 발생 여부는 매우 중요한 차이를 가집니다.

| 구분                         	|             	| 리턴 타입 	| 메서드명      	| 기능                                                                                                  	|
|------------------------------	|-------------	|-----------	|---------------	|-------------------------------------------------------------------------------------------------------	|
| 예외 처리 기능 미포함 메서드 	| 데이터 추가 	| boolean   	| add(E item)   	| 매개변수의 item을 Queue에 추가                                                                        	|
|                              	| 데이터 확인 	| E         	| element()     	| 가장 상위에 있는 원소값 리턴(데이터는 변화 없음, 데이터가 하나도 없을 때 NoSuchElementException 발생) 	|
|                              	| 데이터 추출 	| E         	| remove()      	| 가장 상위에 있는 원소값 꺼내기(꺼낼 데이터가 없을 때 NoSuchElementException 발생)                     	|
| 예외 처리 기능 포함 메서드   	| 데이터 추가 	| boolean   	| offer(E item) 	| 매개변수의 item을 Queue에 추가                                                                        	|
|                              	| 데이터 확인 	| E         	| peek()        	| 가장 상위에 있는 원소값 리턴(데이터는 변화 없음, 데이터가 하나도 없을 때 null을 리턴)                 	|
|                              	| 데이터 추출 	| E         	| poll()        	| 가장 상위에 있는 원소값 꺼내기(꺼낼 데이터가 없을 때 null을 리턴)                                     	|

6개의 메서드 중 add() 메서드만 java.util.Collection 인터페이스에 정의되어 있고, 나머지는 모두 java.util.Queue 인터페이스에 정의되어 있습니다.

> 실제 자바 API 문서에서 peek()와 poll() 메서드의 정의를 확인해 보면, 예외 처리를 하는 대신 if 조건문을 사용해 데이터가 없을 때 null을 리턴하도록 작성되어 있습니다.

아래는 `Queue<E>` 컬렉션의 주요 메서드를 활용한 예시 코드입니다.

```java
// package
import java.util.LinkedList;
import java.util.Queue;

public class QueueMethod {
    public static void main(String[] args) {
        // 1. 예외 처리 기능 미포함 메서드
        Queue<Integer> queue1 = new LinkedList<Integer>();
//        System.out.println(queue1.element());     // NoSuchElementException
        // 1-1. add(E item)
        queue1.add(3);
        queue1.add(4);
        queue1.add(5);
        // 1-2. element()
        System.out.println(queue1.element());
        // 1-3. remove()
        System.out.println(queue1.remove());
        System.out.println(queue1.remove());
        System.out.println(queue1.remove());
//        System.out.println(queue1.remove());      // NoSuchElementException
        System.out.println();
        // 2. 예외 처리 기능 포함 메서드
        Queue<Integer> queue2 = new LinkedList<Integer>();
        System.out.println(queue2.peek());
        // 2-1. offer(E item)
        queue2.offer(3);
        queue2.offer(4);
        queue2.offer(5);
        // 2-2. E peek()
        System.out.println(queue2.peek());
        // 2-3. E poll()
        System.out.println(queue2.poll());
        System.out.println(queue2.poll());
        System.out.println(queue2.poll());
        System.out.println(queue2.poll());
    }
}
```
output
```
3
3
4
5

null
3
3
4
5
null
```

