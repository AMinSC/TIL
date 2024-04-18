# 컬렉션 프레임워크_02 (SET)

## `Set<E>` 컬렉션 인터페이스

### `Set<E>` 컬렉션의 특징
`Set<E>`는 동일한 타입의 묶음이라는 특징은 그대로 가지고 있지만, 인덱스 정보를 포함하고 있지 않은 집합의 개념과 같은 컬렉션입니다.
인덱스 정보가 없기 때문에 데이터를 중복해 저장하면 중복된 데이터중 특정 데이터를 지칭해 꺼낼 방법이 없기 때문에 중복 저장을 허용하지 않습니다.

### `Set<E>`의 주요 메서드
`Set<E>`에는 데이터의 추가, 삭제, 정보 추출 그리고 배열로 변환하는 메서드들이 있습니다.
다만, 데이터의 인덱스를 가지고 있지 않기 때문에 `List<E>`의 메서드에서 인덱스가 포함된 메서드는 제거되었습니다.

| 구분                  	| 리턴 타입   	| 메서드명                          	| 기능                                                       	|
|-----------------------	|-------------	|-----------------------------------	|------------------------------------------------------------	|
| 데이터 추가           	| boolean     	| add(E element)                    	| 매개변수로 입력된 원소를 리스트에 추가                     	|
|                       	| boolean     	| addAll(Collection<? Extends E> c) 	| 매개변수로 입력된 컬렉션 전체를 추가                       	|
| 데이터 삭제           	| boolean     	| remove(Object o)                  	| 원소 중 매개변수 입력과 동일한 객체 삭제                   	|
|                       	| void        	| clear()                           	| 전체 원소 삭제                                             	|
| 데이터 정보 추출      	| boolean     	| isEmpty()                         	| `Set<E>`객체가 비어 있는지 여부를 리턴                       	|
|                       	| boolean     	| contains(Object o)                	| 매개변수로 입력된 원소가 있는지 여부를 리턴                	|
|                       	| int         	| size()                            	| 리스트 객체 내에 포함된 원소의 개수                        	|
|                       	| Iterator<E> 	| iterator()                        	| `Set<E>` 객체 내의 데이터를 연속해 꺼내는 Iterator 객체 리턴 	|
| `Set<E>` 객체 배열 반환 	| Object[]    	| toArray()                         	| 리스트를 Object 배열로 반환                                	|
|                       	| T[]         	| toArray(T[] t)                    	| 입력매개변수로 전달한 타입의 배열로 변환                   	|

- constains(Object o): 해당 `Set<E>` 매개변수로 넘어온 데이터가 객체 내에 포함되어 있는지를 불리언값으로 리턴합니다.
- iterator(): `Iterator<E>` 객체를 리턴하는데, 이 객체는 `Set<E>` 객체에서 데이터를 1개씩 꺼내는 기능을 포함하고 있습니다.
`Set<E>`는 for문으로 인덱스 값을 바꿔가면서 데이터를 출력할 수 있었던 `List<E>`와 달리 인덱스 정보를 갖고 있지 않으므로 일반적인 for문으로 데이터를 꺼낼 수 없습니다.

- `Set<E>` 인터페이스를 상속한 구현 클래스는 아래와 같습니다.
    - `HashSet<E>`, `LinkedHashSet<E>`, `TreeSet<E>`

### `HashSet<E>` 구현 클래스
`HashSet<E>`은 `Set<E>` 인터페이스의 대표적인 구현 클래스입니다.
`HashSet<E>` 컬렉션도 저장 용량(capacity)을 동적으로 관리하며, 기본 생성자로 생성할 때 기본값은 16입니다.

- 데이터 추가하기 - add()
    - `HashSet<E>`은 모든 데이터를 하나의 주머니에 넣어 관리하므로 입력 순서와 다르게 출력될 수 있습니다.
- 데이터 삭제하기 - remove(), clear()
- 데이터 정보 추출하기 - isEmpty(), contains(), size(), iterator()
    - `Iterator<T>`의 대표적인 메서드
        | 리턴 타입 	| 메서드    	| 기능                                               	|
        |-----------	|-----------	|----------------------------------------------------	|
        | boolean   	| hasNext() 	| 다음으로 가리킬 원소의 존재 여부를 불리언으로 리턴 	|
        | E         	| next()    	| 다음 원소 위치로 가서 읽은 값을 리턴               	|
    - hasNext() 메서드는 다음으로 가리킬 원소의 존재 여부를 불리언값으로 리턴하며, next() 메서드는 다음 원소 위치로 가서 읽은 값을 리턴합니다.
    여기서 주의해야할 점은 최초 `Iterator<E>` 객체가 생성되면 이 객체가 가리키고 있는 위치는 첫 원소 위치가 아닌 첫 원소 바로 이전의 위치값이라는 것입니다.
    따라서, 첫 번째 원소값을 읽으려면 iterator().next() 를 실행해야 합니다.
    - `HashSet<E>`의 각 데이터를 꺼내기 위해 iterator() 메서드 대신, for-each 구문을 사용할 수도 있습니다.
- 배열로 변환하기 - toArray(), toArray(T[] t)
    - `List<E>`와 다른 점은 `HashSet<E>`의 특성상 입출력 순서가 다를 수 있습니다.

아래는 메서드를 응용한 `HashSet<E>` 예시 코드입니다.

```java
// package
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class HashSetMethod {
    public static void main(String[] args) {
        Set<String> hSet1 = new HashSet<>();
        // 1. add(E element)
        hSet1.add("가");
        hSet1.add("나");
        hSet1.add("다");
        System.out.println(hSet1.toString());
        // 2. addAll(다른 set 객체)
        Set<String> hSet2 = new HashSet<>();
        hSet2.add("나");
        hSet2.add("다");
        hSet2.addAll(hSet1);
        System.out.println(hSet2.toString());
        // 3. remove(Object o)
        hSet2.remove("나");
        System.out.prinltn(hSet2.toString());
        // 4. clear()
        hSet2.clear();
        System.out.println(hSet2.toString());
        // 5. isEmpty()
        System.out.println(hSet2.isEmpty());
        // 6. contains(Object o)
        Set<String> hSet3 = new HashSet<>();
        hSet.add("가");
        hSet.add("나");
        hSet.add("다");
        System.out.println(hSet3.constain("나"));
        System.out.println(hSet3.constain("라"));
        // 7. size()
        System.out.println(hSet3.size());
        // 8. iterator()
        Iterator<String> iterator = hSet3.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        // 9. toArray()
        Object[] objArray = hSet3.toArray();
        System.out.println(Arrays.toString(objArray));
        // 10-1. toArray(T[] t)
        String[] strArray1 = hSet3.toArray(new String[0]);
        System.out.println(Arrays.toString(strArray1));
        // 10-2. toArray(T[] t)
        String[] strArray2 = hSet3.toArray(new String[5]);
        System.out.println(Arrays.toString(strArray2));
    }
}
```
output
```
[가, 나]
[가, 나, 다]
[가, 다]
[]
true
true
false
3
가
다
나
[가, 다, 나]
[가, 다, 나]
[가, 다, 나, null, null]
```

#### `HashSet<E>`의 중복 확인 매커니즘
`HashSet<E>`은 중복된 데이터를 허용하지 않는다고 했습니다.
여기서 말하는 중복된 데이터의 기준이 무엇인지 정의할 필요가 있습니다.
보통 일반사람이 느끼기에는 동일한 값(예를 들어 3, 3)으로 보이고 중복이 되지 않는다고 생각하지만, `HashSet<E>`은 값을 비교할 때 equals()메서드로 비교하게 되고, equals()는 객체의 주소값을 비교하기 때문에 동일하지 않은 값으로 인식하게 됩니다.

따라서 중복값을 제거하기 위해서는 equlas() 메서드와 `객체가 저장된 번지를 기준으로 생성된 정수형 고유값인 해시코드`를 나타내는 hashCode() 메서드를 오버라이딩하여 재 정의해줘야 합니다.

아래 예시 코드로 중복 확인 매커니즘을 확인해보겠습니다.

```java
// package
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

class A {
    int data;
    public A(int data) {
        this.data = data;
    }
}
class B {
    int data;
    public B(int data) {
        this.data = data;
    }
    @Override
    public boolean equals(Object obj) {
        if (obj instanceof B) {
            this.data = ((B)obj).data;
            return true;
        }
        return false;
    }
}
class C {
    int data;
    public C(int data) {
        this.data = data;
    }
    @override
    public boolean equals(Object obj) {
        if (obj instanceof C) {
            this.data = ((C)obj).data;
            return true;
        }
        return false;
    }
    @override
    public int hashCode() {
        return Object.hash(data);
    }
}
public class HashSetMachanism {
    public static void main(String[] args) {
        // 1. 어떤 것도 오버라이딩하지 않음
        Set<A> hashSet1 = new HashSet<>();
        A a1 = new A(3);
        A a2 = new A(3);
        System.out.println(a1 == a2);
        System.out.println(a1.equals(a2));
        System.out.println(a1.hashCode() + ", " + a2.hashCode());
        hashSet1.add(a1);
        hashSet1.add(a2);
        System.out.println(hashSet1.siez());
        System.out.println();
        // 2. equals() 메서드만 오버라이딩
        Set<B> hashSet2 = new HashSet<>();
        B b1 = new B(3);
        B b2 = new B(3);
        System.out.println(b1 == b2);
        System.out.println(b1.equals(b2));
        System.out.println(b1.hashCode() + ", " + b2.hashCode());
        hashSet1.add(b1);
        hashSet1.add(b2);
        System.out.println(hashSet2.siez());
        System.out.println();
        // 3. equalse(), hashCode() 메서드 오버라이딩
        Set<C> hashSet3 = new HashSet<>();
        C c1 = new C(3);
        C c2 = new C(3);
        System.out.println(c1 == c2);
        System.out.println(c1.equals(c2));
        System.out.println(c1.hashCode() + ", " + c2.hashCode());
        hashSet1.add(c1);
        hashSet1.add(c2);
        System.out.println(hashSet3.siez());
        System.out.println();
    }
}
```
output
```
false
false
2018699554, 1311053135
2

false
true
118352462, 1550089733
2

false
true
24, 24
1
```


### `LinkedHashSet<E>` 구현 클래스
`LinkedHashSet<E>`은 `HashSet<E>`의 자식 클래스로 `HashSet<E>`의 모든 기능에 데이터 간의 연결 정보만을 추가로 갖고 있는 컬렉션 입니다.
즉, 입력된 순서를 기억하고 있습니다.
따라서, `LinkedHashSet<E>`은 출력 순서가 항상 입력 순서와 동일한 특징을 가지고 있습니다.
다만, `List<E>`처럼 중간에 데이터를 추가하거나 특정 순서에 저장된 값을 가져오는 것은 불가능합니다.

`LinkedHashSet<E>`의 모든 메서드 활용 방법은 출력 순서가 입력 순서와 동일하다는 점을 제외하ㅗ는 부모 클래스인 `HashSet<E>`과 동일합니다.


### `TreeSet<E>` 구현 클래스
`TreeSet<E>`은 공통적인 `Set<E>`의 기능에, 크기에 따른 정렬 및 검색 기능이 추가된 컬렉션입니다.

저장된 데이터를 출력할 때 `HashSet<E>`은 입력 순서와 다를 수 있고, `LinkedHashSet<E>`은 항상 입력 순서와 동일하지만, `TreeSet<E>`은 데이터를 입력 순서와 상관없이 크기순으로 출력합니다.
따라서 `HashSet<E>`에서 두 객체가 같은지 비교했다면, `TreeSet<E>`은 두 객체의 크기를 비교해야 합니다.

`TreeSet<E>`은 다른 구현 클래스와 달리 `NavigableSet<E>`과 `SortedSet<E>`을 부모 인터페이스로 두고 있습니다.
해당 인터페이스는 정렬과 검색 기능이 추가로 정의되어 있으며 꼭 `TreeSet<E>`으로 선언해야 고나련 메서드를 호출할 수 있습니다.

#### `TreeSet<E>`의 주요 메서드
`TreeSet<E>`도 결국 `Set<E>`의 구현 클래스이므로 다른 구현 클래스처럼 `Set<E>`의 모든 메서드를 사용ㄴ할 수 있고, 활용법 또한 동일합니다.
따라서 이번에는 `TreeSet<E>`에서 추가된 정렬과 검색 관련 메서드에 대해서만 알아보겠습니다.
이들 메서드는 크게 데이터 검색, 꺼내기, 구분 집합 생성 그리고 정렬로 나눌 수 있습니다.

| 구분                  	| 리턴 타입       	| 메서드명                                                                       	| 기능                                                                                                                                                                     	|
|-----------------------	|-----------------	|--------------------------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 데이터 검색           	| E               	| first()                                                                        	| Set 원소 중 가장 작은 원소값 리턴                                                                                                                                        	|
|                       	| E               	| last()                                                                         	| Set 원소 중 가장 큰 원소값 리턴                                                                                                                                          	|
|                       	| E               	| lower(E element)                                                               	| 매개변수로 입력된 원소보다 작은, 가장 큰 수                                                                                                                              	|
|                       	| E               	| higher(E element)                                                              	| 매개변수로 입력된 원소보다 큰, 가장 작은 수                                                                                                                              	|
|                       	| E               	| floor(E element)                                                               	| 매개변수로 입력된 원소보다 같거나 작은 가장 큰 수                                                                                                                        	|
|                       	| E               	| ceiling(E element)                                                             	| 매개변수로 입력된 원소보다 같거나 큰 가장 작은 수                                                                                                                        	|
| 데이터 꺼내기         	| E               	| pollFirst()                                                                    	| Set 원소들 중 가장 작은 원소값을 꺼내 리턴                                                                                                                               	|
|                       	| E               	| pollLast()                                                                     	| Set 원소들 중 가장 큰 원소값을 꺼내 리턴                                                                                                                                 	|
| 데이터 부분 집합 생성 	| SortedSet<E>    	| headSet(E toElement)                                                           	| toElement 미만인 모든 원소로 구성된 Set을 리턴(ToElement 미포함)                                                                                                         	|
|                       	| NavigableSet<E> 	| headSet(E ToElement, boolean inclusive)                                        	| toElement 미만/이하인 모든 원소로 구성된 Set을 리턴(inclusive=ture면 toElement 포함, inclusive=false면 toElement 미포함)                                                 	|
|                       	| SortedSet<E>    	| tailSet(E fromElement)                                                         	| toElement 이상인 모든 원소로 구성된 Set을 리턴(fromElement 포함)                                                                                                         	|
| 데이터 부분 집합 생성 	| NavigableSet<E> 	| tailSet(E fromElement, boolean inclusive)                                      	| fromElement 초과/이상인 모든 원소로 구성된 Set을 리턴(inclusive=true면 fromElement 포함, inclusive=false면 fromElement 미포함)                                           	|
|                       	| SortedSet<E>    	| subSet(E fromElement, E toElement)                                             	| fromElement 이상 toElement 미만인 원소들로 이뤄진 Set을 리턴(fromElement 포함, toElement미포함)                                                                          	|
|                       	| NavigableSet<E> 	| subSet(E fromElement, boolean frominclusive, E toElement, boolean toinclusive) 	| fromElement 초과/이상 toElement 미만/이하인 원소들로 이뤄진 Set을 리턴(fromclusive=true/false면 fromElement 포함/미포함, toinclusive=true/false면 toElement 포함/미포함) 	|
| 데이터 정렬           	| NavigableSet<E> 	| descendingSet()                                                                	| 내림차순의 의미가 아닌, 현재 정렬 기준을 반대로 변환                                                                                                                     	|

> descending의 사전적인 의미가 내림차순이라고 해서 내림차순으로 정렬하는 것이 아니라는 점에 유의해야 합니다.


`TreeSet<E>`의 주요 메서드를 활용한 예시 코드입니다.
```java
// package
import java.util.NavigableSet;
import java.util.SortedSet;
import java.util.TreeSet;

public class TreeSetMethod_1 {
    public static void main(String[] args) {
        TreeSet<Integer> treeSet = new TreeSet<>();
        for (int i = 50; i > 0; i -= 2) {
            treeSet.add(i);
        }
        System.out.println(treeSet.toString());
        // 1. first()
        System.out.println(treeSet.first());
        // 2. last()
        System.out.println(treeSet.last());
        // 3. loew(E element)
        System.out.println(treeSet.lower(26));
        // 4. higher(E element)
        System.out.println(treeSet.higher(26));
        // 5. floor(E element)
        System.out.println(treeSet.floor(25));
        System.out.println(treeSet.floor(26));
        // 6. ceiling(E element)
        System.out.println(treeSet.ceiling(25));
        System.out.println(treeSet.ceiling(26));
        System.out.println();
        // 7. pollFirst()
        int treeSetSize = treeSet.size();
        System.out.println(treeSetSize);
        for (int i = 0; i < treeSetSize; i++) {
            System.out.println(treeSet.pollFirst() + " ");
        }
        System.out.println();
        System.out.println(treeSet.size());
        // 8. pollLast()
        for (int i = 50; i > 0; i -= 2) {
            treeSet.add(i);
        }
        treeSetSize = treeSet.size();
        for (int i = 0; i < treeSetSize; i++) {
            System.out.println(treeSet.pollLast() + " ");
        }
        System.out.println();
        System.out.println(treeSet.size());
        // 9. SortedSet<E> headSet(E element)
        for (int i = 50; i > 0; i -= 2) {
            treeSet.add(i);
        }
        SortedSet<Integer> sSet = treeSet.headSet(20);
        System.out.println(sSet.toString());
        // 10. NavigableSet<E> headSet(E element, boolean inclusive)
        NavigableSet<Integer> nSet = treeSet.headSet(20, true);
        System.out.println(nSet.toString());
        nSet = treeSet.headSet(20, false);
        System.out.println(nSet.toString());
        // 11. SortedSet<E> tailSet(E element)
        sSet = treeSet.tailSet(20);
        System.out.println(sSet.toString());
        // 12. NavigableSet<E> tailSet(E element, boolean inclusive)
        nSet = treeSet.tailSet(20, true);
        System.out.println(nSet.toString());
        nSet = treeSet.tailSet(20, false);
        System.out.println(nSet.toString());
        // 13. SortedSet<E> subSet(E element, E element)
        sSet = treeSet.subSet(10, 20);
        System.out.println(sSet.toString());
        // 14. NavigableSet<E> subSet(E element, boolean inclusive, E element, boolean inclusive)
        nSet = treeSet.subSet(10, true, 20, false);
        System.out.println(nSet.toString());
        nSet = treeSet.subSet(10, false, 20, true);
        System.out.println(nSet.toString());
        // 15. NavigableSet<E> descendingSet()
        System.out.println(treeSet);
        NavigableSet<Integer> descendingSet = treeSet.descendingSet();
        System.out.println(descendingSet);
        descendingSet = descendingSet.descendingSet();
        System.out.println(descendingSet);
    }
}
```
putput
```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
2
50
24
28
24
26
26
26

25
2 
4 
6 
8 
10 
12 
14 
16 
18 
20 
22 
24 
26 
28 
30 
32 
34 
36 
38 
40 
42 
44 
46 
48 
50 

0
50 
48 
46 
44 
42 
40 
38 
36 
34 
32 
30 
28 
26 
24 
22 
20 
18 
16 
14 
12 
10 
8 
6 
4 
2 

0
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[10, 12, 14, 16, 18]
[10, 12, 14, 16, 18]
[12, 14, 16, 18, 20]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
```

