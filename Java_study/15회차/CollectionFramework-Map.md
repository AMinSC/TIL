# 컬렉션 프레임워크_03 (Map)
`List<E>`, `Set<E>`은 `Collection<E>` 인터페이스를 상속받는 반면, `Map<k, V>`은 별도의 인터페이스로 존재합니다.
따라서 저장의 형태와 방식이 앞의 두 컬렉션과 다릅니다.

## `Map<K, V>` 컬렉션의 특징
### Key와 Value 한 쌍으로 데이터를 저장
`Map<K, V>` 컬렉션은 Key와 Value의 한 쌍으로 데이터를 저장합니다.
이 때 한 쌍의 데이터를 `엔트리(entry)`라고 하며, Map.Entry 타입으로 정의됩니다. 따라서 `Map<K, V>`은 데이터를 엔트리 단위로 입력받습니다.

### Key는 중복 저장 불가, Value는 중복 가능
데이터를 구분하는 기준이 index가 아닌 Key이기 때문에 Key값은 중복이 불가능 합니다.
다만, index의 원소값은 중복이 되는 것처럼 value값은 중복이 가능합니다.

## `Map<K, V>` 인터페이스의 주요 메서드
`Map<K, V>` 인터페이스의 메서드를 살펴보면 크게 데이터의 추가, 변경, 정보 추출 및 삭제로 나눌 수 있습니다.

| 구분             	| 리턴 타입        	| 메서드명                                	| 기능                                                                                                     	|
|------------------	|------------------	|-----------------------------------------	|----------------------------------------------------------------------------------------------------------	|
| 데이터 추가      	| V                	| put(k Key, V Value)                     	| 입력매개변수의 (Key, Value)를 Map객체에 추가                                                             	|
|                  	| void             	| putAll(Map<? extends K, ? extends V> m) 	| 입력매개변수의 Map 객체를 통째로 추가                                                                    	|
| 데이터 변경      	| V                	| replace(K Key, V Value)                 	| Key에 해당하는 값을 Value 값으로 변경(old 값 리턴)(단, 해당 Key값이 없으면 null 리턴)                    	|
|                  	| boolean          	| replace(K Key, V oldValue, V new Value) 	| (Key, oldValue)의 쌍을 갖는 엔트리에서 oldValue를 newValue로 변경(단, 해당 엔트리가 없으면 false를 리턴) 	|
| 데이터 정보 추출 	| V                	| get(Object key)                         	| 매개변수의 Key값에 해당하는 oldValue를 리턴                                                              	|
|                  	| boolean          	| containsKey(Object key)                 	| 매개변수의 Key 값이 포함되어 있는지 여부                                                                 	|
|                  	| boolean          	| containsValue(Object value)             	| 매개변수의 Value 값이 포함되어 있는지 여부                                                               	|
|                  	| `Set<K>`           	| keySet()                                	| Map 데이터들 중 Key들만 뽑아 Set 객체로 리턴                                                             	|
|                  	| `Set<Entry<K, V>>` 	| entrySet()                              	| Map의 각 엔트리들을 Set 객체로 담아 리턴                                                                 	|
|                  	| int              	| size()                                  	| Map에 포함된 엔트리의 개수                                                                               	|
| 데이터 삭제      	| V                	| remove(Object key)                      	| 입력매겨변수의 Key를 갖는 엔트리 삭제(단, 해당 Key가 없으면 아무런 동작을 하지 않음)                     	|
|                  	| boolean          	| remove(Object key, Object value)        	| 입력매개변수의 (key, value)를 갖는 엔트리 삭제(단, 해당 엔트리가 없으면 아무런 동작을 하지 않음)         	|
|                  	| void             	| clear()                                 	| Map 객체 내의 모든 데이터 삭제                                                                           	|


KeySet()은 `Map<K, V>` 데이터 쌍들 중에서 Key만을 뽑아 `Set<E>`로 리턴합니다.
`Map<K, V>`는 Key 값들을 `Set<E>` 형태로 관리합니다. 따라서 Key 값의 중복이 불가능한 이유입니다.
Map 데이터를 1개씩 꺼낼 때 일반적으로 이 KeySet()로 전체 Key를 추출하고, 각 Key값에 따라 Value값을 읽습니다.

`Map<K, V>` 역시 인터페이스이기 때문에 객체를 생성하기 위해서는 하위 클래스에서 위의 모든 메서드를 구현해야 합니다.
`Map<K, V>` 인터페이스의 대표적인 구현 클래스로는 `HashMap<K, V>`, `LinkedHashMap<K, V>`, `HashTable<K, V>`, `TreeMap<K, V>`를 들 수 있습니다.

> `HashMap<K, V>`와 `HashTable<K, V>`는 Key값을 `HashSet<E>`로 관리하고, `LinkedHashMap<K, V>`와 `TreeMap<K, V>`는 Key 값을 각각 `LinkedHashSet<E>` 및 `TreeSet<E>`로 관리합니다.


## `HashMap<K, V>`
`HashMap<K, V>`는 `Map<K, V>`의 대표적인 구현 클래스로, Key 값의 중복을 허용하지 않습니다.
`Key 값의 중복 여부를 확인하는 메커니즘은 HashSet<E> 때와 완벽히 동일합니다.`
즉, 두 Key 객체의 hashCode() 값이 같고, equals() 메서드가 true를 리턴하면 같은객체로 인식하며, 이외에는 서로 다른 객체로 간주해 각각의 Key값으로 등록할 수 있습니다.

`HashMap<K, V>` 객체는 개념상으로 Key값을 `HashSet<E>`로 구현한 `Map<K, V>` 객체입니다.
따라서 Key 값이 `HashSet<E>`의 특성이 있으므로 입출력 순서는 동일하지 않을 수도 있습니다.

초기 저장 용량의 기본값은 16이고, 원소의 개수가 16을 넘어가면 자동으로 늘어납니다.

### `HashMap<K, V>`의 주요 메서드
`HashMap<K, V>`의 주요 메서드를 활용한 예시 코드는 아래와 같습니다.

```java
// package
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapMethod {
    public static void main(String[] args) {
        Map<Integer, String> hMap1 = new HashMap<Integer, String>();
        // 1. put(K key, V value)
        hMap1.put(2, "나다라");
        hMap1.put(1, "가나다");
        hMap1.put(3, "다라마");
        System.out.println(hMap1.toString());
        // 2. putAll(다른 맵 객체)
        Map<Integer, String> hMap2 = new HashMap<Integer, String>();
        hMap2.putAll(hMap1);
        System.out.println(hMap2.toString());
        // 3. replace(K key, V value)
        hMap2.replace(1, "가가가");
        hMap2.replace(4, "라라라");     // 동작하지 않음
        System.out.println(hMap2.toString());
        // 4. replace(K key, V oldValue, V newValue)
        hMap2.replace(1, "가가가", "나나나");
        hMap2.replace(2, "다다다", "라라라");
        System.out.println(hMap2.toString());
        // 5. V get(Object key)
        System.out.println(hMap2.get(1));
        System.out.println(hMap2.get(2));
        System.out.println(hMap2.get(3));
        // 6. containsKey(Object key)
        System.out.println(hMap2.containsKey(1));
        System.out.println(hMap2.containsKey(5));
        // 7. containsValue(Object value)
        System.out.println(hMap2.containsValue("나나나"));
        System.out.println(hMap2.containsValue("다다다"));
        // 8. Set<K> keySet()
        Set<Integer> keySet = hMap2.keySet();
        System.out.println(keySet.toString());
        // 9. Set<Map.Entry<K, V>> entrySet()
        Set<Map.Entry<Integer, String>> entrySet = hMap2.entrySet();
        System.out.println(entrySet.toString());
        // 10. size()
        System.out.println(hMap2.size());
        // 11. remove(Object key)
        hMap2.remove(1);
        hMap2.remove(4);
        // 12. remove(Object key, Object value)
        hMap2.remove(2, "나다라");
        hMap2.remove(3, "다다다");
        System.out.println(hMap2.toString());
        // 13. clear()
        hMap2.clear();
        System.out.println(hMap2.toString());
    }
}
```
output
```
{1=가나다, 2=나다라, 3=다라마}
{1=가나다, 2=나다라, 3=다라마}
{1=가가가, 2=나다라, 3=다라마}
{1=나나나, 2=나다라, 3=다라마}
나나나
나다라
다라마
true
false
true
false
[1, 2, 3]
[1=나나나, 2=나다라, 3=다라마]
3
{3=다라마}
{}
```

> `HashMap<K, V>`에서 Key의 중복을 확인하는 메커니즘은 `HashSet<E>`에서의 중복 메커니즘과 동일합니다.

## `HashTable<K, V>`
`HashMap<K, V>` 구현 클래스가 단일 쓰레드에 적합한 반면, `HashTable<K, V>`은 멀티 쓰레드에 안전성을 가집니다.
즉, 하나의 `Map<k, V>` 객체를 2개의 쓰레드가 동시에 접근할 때도 모든 내부의 주요 메서드가 `동기화(synchronized)`메서드로 구현되어 있으므로 멀티 쓰레드에서도 안전하게 동작합니다.

### `HashTable<K, V>`의 주요 메서드
`HashTable<K, V>`는 `HashMap<K, V>`와 비교해 멀티 쓰레드에서도 안전하다는 특징 말고는 완벽히 `HashMap<K, V>`와 동일한 특징을 가집니다.


## `LinkedHashMap<K, V>`
`LinkedHashMap<K, V>`는 `HashMap<K, V>`의 기본적인 특성에 입력 데이터의 순서 정보를 추가로 가지고 있는 컬렉션입니다.
따라서 저장 데이터를 출력하면 항상 입력된 순서대로 출력됩니다.
`HashMap<K, V>`는 Key를 `HashSet<E>`으로 관리하는 반면, `LinkedHashMap<K, V>`의 Key는 `LinkedHashSet<E>`으로 관리합니다.

### `LinkedHashMap<K, V>`의 주요 메서드
`LinkedHashMap<K, V>`에서 사용되는 메서드 또한 출력이 입력의 순으로 나오는 것을 제외하면 `HashMap<K, V>`과 완벽히 동일합니다.

## `TreeMap<K, V>`
`Map<K, V>` 인터페이스의 마지막 구현 클래스는 `TreeMap<K, V>`로 `Map<K, V>`의 기본 기능에 정렬 및 검색 기능이 추가된 컬렉션입니다.
따라서 입력 순서와 관계없이 데이터를 Key값의 크기 순으로 저장하기 때문에 반드시 Key 객체의 크기 비교의 기준을 정의해줘야 합니다.

`TreeSet<E>`의 상속 구조와 비슷화게 `TreeMap<K, V>`도 `SortedMap<K, V>`과 `NavigableMap<K, V>` 인터페이스의 자식 클래스입니다.

### `TreeMap<K, V>`의 주요 메서드
`TreeMap<K, V>`에서 추가로 사용할 수 있는 정렬과 검색 관련 메서드만 다룰 예정이며, `TreeSet<E>`과 매우 비슷하지만 단지 데이터가 (Key, Value)로 이뤄진 쌍의 엔트리 형태로 저장되기 때문에 Key와 엔트리에 데이터를 검색하거나 추출하는 메서드가 포함된다는 점에만 차이가 있습니다.

| 구분                  	| 리턴 타입          	| 메서드명                                                               	| 기능                                                                                                                                                                                	|
|-----------------------	|--------------------	|------------------------------------------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| 데이터 검색           	| K                  	| firstKey()                                                             	| Map 원소 중 가장 작은 Key값 리턴                                                                                                                                                    	|
|                       	| Map.Entry<K, V>    	| firstEntry()                                                           	| Map 원소 중 가장 작은 Key 값을 가진 엔트리 리턴                                                                                                                                     	|
|                       	| K                  	| lastKey()                                                              	| Map 원소 중 가장 큰 Key 값 리턴                                                                                                                                                     	|
|                       	| Map.Entry<K, V>    	| lastEntry()                                                            	| Map 원소 중 가장 큰 Key 값을 가진 엔트리 리턴                                                                                                                                       	|
|                       	| K                  	| lowerKey(K key)                                                        	| 매개변수로 입력된 Key 값보다 작은 Key 값 중 가장 큰 Key 값 리턴                                                                                                                     	|
|                       	| Map.Entry<K, V>    	| lowerEntry(K key)                                                      	| 매개변수로 입력된 Key값보다 작은 Key 값 중 가장 큰 Key 값은 가진 엔트리 리턴                                                                                                        	|
|                       	| K                  	| higherKey(K key)                                                       	| 매개변수로 입력된 Key 값보다 큰 Key 값 중 가장 작은 Key 값 리턴                                                                                                                     	|
|                       	| Map.Entry<K, V>    	| higherEntry(K key)                                                     	| 매개변수로 입력된 Key 값보다 큰 Key 값 중 가장 작은 Key 값을 가진 엔트리 리턴                                                                                                       	|
| 데이터 추출           	| Map.Entry<K, V>    	| pollFirstEntry()                                                       	| Map 원소 중 가장 작은 Key 값을 가진 엔트리를 꺼내 리턴                                                                                                                              	|
|                       	| Map.Entry<K, V>    	| pollLastEntry()                                                        	| Map 원소 중 가장 큰 Key  값을 가진 엔트리를 꺼내 리턴                                                                                                                               	|
| 데이터 부분 집합 생성 	| SortedMap<K, V>    	| headMap(K toKey)                                                       	| toKey 미만의 Key 값을 가진 모든 엔트리를 포함한 Map 객체 리턴(toKey 미포함)                                                                                                         	|
|                       	| NavigableMap<K, V> 	| headMap(K toKey, boolean inclusive)                                    	| toKey 미만/이하의 Key 값을 가진 모든 엔트리를 포함한 Map 객체 리턴(inclusive=true면 toKey 포함, inclusive=false면 toKey 미포함)                                                     	|
|                       	| SortedMap<K, V>    	| tailMap(K fromKey)                                                     	| fromKey 이상인 Key 값을 가진 모든 엔트리를 포함한 Map 객체 리턴(fromKey 포함)                                                                                                       	|
|                       	| NavigableMap<K, V> 	| tailMap(K fromKey, boolean inclusive)                                  	| fromKey 초과/이상인 Key 값을 가진 모든 엔트리를 포함한 Map 객체 리턴(inclusive=true면 fromKey 포함, inclusive=false면 fromKey 미포함)                                               	|
|                       	| SortedMap<K, V>    	| subSet(K fromKey, K toKey)                                             	| fromKey 이상 toKey 미만의 Key값을 가진 모든 엔트리를 포함한 Map 객체를 리턴(fromKey 포함, toKey 미포함)                                                                             	|
|                       	| NavigableMap<K, V> 	| subSet(K fromKey, boolean fromInclusive, K toKey, boolean toInclusive) 	| fromKey 초과/이상 toKey 미만/이하인 Key 값을 가진 모든 엔트리를 포함한 Map 객체를 리턴(fromInclusive=true/false 면 fromKey 포함/미포함, toInclusive=true/false면 toKey 포함/미포함) 	|
| 데이터 정렬           	| NavigableMap<K, V> 	| descendingKeySet()                                                     	| Map에 포함된 모든 Key 값의 정렬을 반대로 변환한 Set 객체 리턴                                                                                                                       	|
|                       	| NavigableMap<K, V> 	| descendingMap()                                                        	| Map에 포함된 모든 Key 값의 정렬을 반대로 변환한  Map 객체 리턴                                                                                                                      	|


`TreeMap<K, V>` 클래스의 주요 메서드를 활용한 예시 코드는 아래와 같습니다.

```java
// package
import java.util.NavigableMap;
import java.util.NavigableSet;
import java.util.SortedMap;
import java.util.TreeMap;

public class TreeMapMethod {
    public static void main(String[] args) {
        TreeMap<Integer, String> treeMap = new TreeMap<Integer, String>();
        for (int i = 20; i > 0; i -= 2) {
            treeMap.put(i, i+" 번째 데이터");
        }
        System.out.println(treeMap.toString());
        // 1. firstKey()
        System.out.println(treeMap.firstKey());
        // 2. firstEntry()
        System.out.println(treeMap.firstEntry());
        // 3. lastKey()
        System.out.println(treeMap.lastKey());
        // 4. lastEntry()
        System.out.println(treeMap.lastEntry());
        // 5. lowerKey(K key)
        System.out.println(treeMap.lowerKey(11));
        System.out.println(treeMap.lowerKey(10));
        // 6. higherKey(K key)
        System.out.println(treeMap.higherKey(11));
        System.out.println(treeMap.higherKey(10));
        // 7. pollFirstEntry()
        System.out.println(treeMap.pollFirstEntry());
        System.out.println(treeMap.toString());
        // 8. pollLastEntry()
        System.out.println(treeMap.pollLastEntry());
        System.out.println(treeMap.toString());
        // 9. SortedMap<K, V> headMap(K toKey)
        SortedMap<Integer, String> sortedMap = treeMap.headMap(8);
        System.out.println(sortedMap);
        // 10. NavigableMap<K, V> headMap(K toKey, boolean inclusive)
        NavigableMap<Integer, String> navigableMap = treeMap.headMap(8, true);
        System.out.println(navigableMap);
        // 11. SortedMap<K, V> tailMap(K toKey)
        sortedMap = treeMap.tailMap(11);
        System.out.println(sortedMap);
        // 12. NavigableMap<K, V> tailMap(K toKey, boolean inclusive)
        navigableMap = treeMap.tailMap(14, false);
        System.out.println(navigableMap);
        // 13. SortedMap<K, V> subMap(K fromKey, K toKey)
        sortedMap = treeMap.subMap(6, 10);
        System.out.println(sortedMap);
        // 14. NavigableMap<K, V> subMap(K toKey, boolean inclusive)
        navigableMap = treeMap.subMap(6, false, 10, true);
        System.out.println(navigableMap);
        // 15. NavigableMap<K, V> descendingKeySet()
        NavigableSet<Integer> navigableSet = treeMap.descendingKeySet();
        System.out.println(navigableSet.toString());
        System.out.println(navigableSet.descendingSet());
        // 16. NavigableMap<K, V> descendingMap()
        navigableMap = treeMap.descendingMap();
        System.out.println(navigableMap.toString());
        System.out.println(navigableMap.descendingMap());
    }
}

```
output
```
{2=2 번째 데이터, 4=4 번째 데이터, 6=6 번째 데이터, 8=8 번째 데이터, 10=10 번째 데이터, 12=12 번째 데이터, 14=14 번째 데이터, 16=16 번째 데이터, 18=18 번째 데이터, 20=20 번째 데이터}
2
2=2 번째 데이터
20
20=20 번째 데이터
10
8
12
12
2=2 번째 데이터
{4=4 번째 데이터, 6=6 번째 데이터, 8=8 번째 데이터, 10=10 번째 데이터, 12=12 번째 데이터, 14=14 번째 데이터, 16=16 번째 데이터, 18=18 번째 데이터, 20=20 번째 데이터}
20=20 번째 데이터
{4=4 번째 데이터, 6=6 번째 데이터, 8=8 번째 데이터, 10=10 번째 데이터, 12=12 번째 데이터, 14=14 번째 데이터, 16=16 번째 데이터, 18=18 번째 데이터}
{4=4 번째 데이터, 6=6 번째 데이터}
{4=4 번째 데이터, 6=6 번째 데이터, 8=8 번째 데이터}
{12=12 번째 데이터, 14=14 번째 데이터, 16=16 번째 데이터, 18=18 번째 데이터}
{16=16 번째 데이터, 18=18 번째 데이터}
{6=6 번째 데이터, 8=8 번째 데이터}
{8=8 번째 데이터, 10=10 번째 데이터}
[18, 16, 14, 12, 10, 8, 6, 4]
[4, 6, 8, 10, 12, 14, 16, 18]
{18=18 번째 데이터, 16=16 번째 데이터, 14=14 번째 데이터, 12=12 번째 데이터, 10=10 번째 데이터, 8=8 번째 데이터, 6=6 번째 데이터, 4=4 번째 데이터}
{4=4 번째 데이터, 6=6 번째 데이터, 8=8 번째 데이터, 10=10 번째 데이터, 12=12 번째 데이터, 14=14 번째 데이터, 16=16 번째 데이터, 18=18 번째 데이터}
```

Key 값의 크기에 따라 오름차순으로 정렬하는 과정에서 적용되는 `TreeMap<K, V>`의 크기비교 메커니즘은 `TreeSet<E>`와 모든 내용이 완벽히 동일합니다.
유일한 차이점은 `TreeMap<K, V>`일 때는 Key 값의 크기를 비교해 정렬을 수행한다는 점입니다.
