# 쓰레드_2

## 쓰레드의 속성
생성한 쓰레드의 객체를 참조하거나 우선순위를 지정하는 것과 같은 쓰레드의 속성 종류와 이를 활용하는 방법을 알아보겠습니다.

### 현재 쓰레드 객체 참좃값 얻어오기
Thread 클래스를 직접 정의하고 객체를 생성해 사용할 때 참조 변수를 이용해 언제든지 쓰레드 객체의 속성(이름 등)을 가져올 수 있습니다.
하지만, 직접 쓰레드 객체를 생성했을 때가 아니거나(자바의 쓰레드 풀 또는 main 쓰레드 등) 객체를 생성할 때 참조 변수를 정의하지 않을 경우에는 (new Thread().start()) 객체를 참조할 수 없게 됩니다.
이처럼 쓰레드 객체를 참조할 수 없을 때 Thread 클래스의 정적 메서드인 currentThread() 메서드를 이용해 현재 쓰레드 객체의 참조값을 얻어올 수 있습니다.

```java
// 현재 쓰레드 객체 참조값 얻어오기
static Thread Thread.currentThread()
```

> 쓰레드 풀(thread-pool)은 멀티 쓰레드 작업을 하기 위해 자바가 미리 생성해 놓은 쓰레드의 모음입니다.


### 실행 중인 쓰레드의 개수 가져오기
여러 개의 쓰레드가 실행되고 있을 때 현재 실행(active)중인 쓰레드의 개수를 알고자 한다면, Thread 클래스 내의 정적 메서드인 activeCount()를 사용해야 합니다.

```java
// 실행 중인 쓰레드의 개수 가져오기
static int Thread.activeCount()
```

activeCount()는 동일한 쓰레드 그룹 내에서 실행 중인 쓰레드의 개수를 리턴합니다.
하나의 쓰레드에서 별도의 지정 없이 새로운 쓰레드를 생성하면 생성된 쓰레드는 생성한 쓰레드와 동일한 쓰레드 그룹에 위치합니다.
여기서 프로그램 실행 시 최초로 생성되는 main 쓰레드는 main 쓰레드 그룹에 속하며, main 쓰레드에서 생성한 쓰레드는 모두 같은 main 쓰레드 그룹에 속한다는 정도만 알아두겠습니다.

### 쓰레드의 이름 지정 및 가져오기
여러 개의 쓰레드를 생성하고 실행하다 보면 각가의 쓰레드를 구분할 필요가 생깁니다.
쓰레드를 구분하는 가장 손쉬운 방법은 쓰레드마다 이름을 부여하는 것입니다.
직접 이름을 부여하려면 Thread 클래스의 인스턴스 메서드인 setName() 메서드를 사용해야 합니다.

```java
// 쓰레드 이름 설정하기
String setName(String name)
```

쓰레드의 이름을 직접 지정하지 않으면 컴파일러가 대신해서 자동으로 부여합니다. 이때 자동으로 부여되는 이름은 Thread-0, Thread-1, ..., Thread-N 처럼 `Thread-숫자`의 형태로 새롭게 생성될 때마다 숫자가 늘어납니다.

setName() 메서드는 인스턴스 메서드이므로 일단 쓰레드 객체를 생성한 후에 적용할 수 있을 것이며, 직접 지정했거나 자동으로 부여된 쓰레드의 이름을 가져올 때는 인스턴스 메서드인 getName()을 사용합니다.

```java
// 쓰레드 이름 가져오기
String getName()
```

```java
// 쓰레드 객체의 속성 다루기
package sec03_threadproperties.EX01_ThreadProperties_1;

public class ThreadProperties_1 {
    public static void main(String[] args) {

        // 객체 참조하기, 쓰레드 개수 가져오기
        Thread curThread = Thread.currentThread();
        System.out.println("현재 쓰레드의 이름 = " + curThread.getName());
        System.out.println("동작하는 쓰레드의 개수 = " + Thread.activeCount());

        // 쓰레드 이름 자동 지정
        for (int i = 0; i < 3; i++) {
            Thread thread = new Thread();
            System.out.println(thread.getName());
            thread.start();
        }

        // 쓰레드 이름 직접 지정
        for (int i = 0; i < 3; i++) {
            Thread thread = new Thread();
            thread.setName(i + "번째 쓰레드");
            System.out.println(thread.getName());
            thread.start();
        }

        // 쓰레드 이름 자동 지정
        for (int i = 0; i < 3; i++) {
            Thread thread = new Thread();
            System.out.println(thread.getName());
            thread.start();
        }

        // 쓰레드의 개수 가져오기
        System.out.println("동작하는 쓰레드의 개수 = " + Thread.activeCount());
    }
}
```

output
```
현재 쓰레드의 이름 = main
동작하는 쓰레드의 개수 = 1
Thread-0
Thread-1
Thread-2
0번째 쓰레드
1번째 쓰레드
2번째 쓰레드
Thread-6
Thread-7
Thread-8
동작하는 쓰레드의 개수 = 5
```


### 쓰레드의 우선순위
모든 쓰레드는 1 ~ 10 사이의 우선순위를 갖고 있습니다. 1이 가장 낮은 순위 값, 10이 가장 높은 순위값입니다. 우선순위를 지정하지 않으면 기본값으로 5의 우선순위를 갖습니다.

다음은 실제 자바 API에서 제공하는 Thread 클래스에 정의된 정적 상수입니다. 대표적으로 수선순위가 1, 5, 10일 때는 각가 정적 상수 Thread.MIN_PRIORITY, Thread.NORM_PRIORITY, Thread.MAX_PRIORITY 값으로 정의되어 있습니다.

```java
// The minimum priority that a thread can have.
public final static int MIN_PRIORITY = 1;
// The default priority that is assigned to a thread.
public final static int NORM_PRIORITY = 5;
// The maximum priority that a thread can have.
public final static int MAX_PRIORITY = 10;
```

이 우선순위는 쓰레드의 동시성과 관계가 있습니다. 만일 2개의 쓰레드가 2개의 CPU 코어에 각각 할당되어 동작하는 쓰레드 병렬성일 때 우선순위는 의미가 없습니다.
2개의 작업이 하나의 CPU코어에서 동작할 때 쓰레드의 동시성에 따라 2개의 작업은 일정 시간 간격으로 번갈아 가면서 실행됩니다.
이때 우선순위가 높으면 상대적으로 더 많은 시간을 할당받게 됩니다.

![priority](asset/thread_priority.png)

만일 동일한 작업량을 가진다면 우선순위가 높은 쓰레드가 먼저 끝날 것입니다.
쓰레드의 우선순위를 지정하거나 지정된 우선순위 값을 가져오는 메서드는 Thread 클래스의 인스턴스 메서드인 setPriority()와 getPriority()가 있습니다.

```java
// 쓰레드 객체의 우선순위 정하기
void setPriority()

// 쓰레드 객체의 우선순위 가져오기
int getPriority()
```

현재 컴퓨터의 CPU 코어 수를 알고 싶을 때는 다음 메서드를 사용해야 합니다.
`public native int availableProcessors()`

> 사용하는 CPU가 하이퍼 쓰레드를 사용할 때 실제 코어 수의 2배를 리턴합니다.
하이퍼 쓰레드는 각 코어에서 둘 이상의 쓰레드를 실행할 수 있는 하드웨어 기술로, 실제 코어 수가 4개이고, 하이퍼 쓰레드를 사용할 때 availableProcessors() 메서드는 8을 리턴합니다.


다음 예제에서는 10억 번의 for 문을 반복한 후 자신의 이름과 우선순위를 출력하는 MyThread 클래스를 정의했습니다.

```java
// 쓰레드의 우선순위
package sec03_threadproperties.EX02_ThreadProperties_2;

class MyThread extends Thread {
    @Override
    public void run() {
        for (long 1 = 0; i < 1000000000; i++) {  // 시간 지연용
            System.out.println(getName() + " 우선순위: " + getPriority())
        }
    }
}

public class ThreadProperties_2 {
    public static void main(String[] args) {

        // CPU 코어 수
        System.out.println("코어 수: " + Runtime.getRuntime().availableProcessors());

        // 우선순위 자동 지정
        for (int i = 0; i < 3; i++) {
            Thread thread = new MyThread();
            thread.start();
        }

        try {Thread.sleep(1000);} catch (InterruptedException e) {}

        // 우선순위 직접 지정
        for (int i = 0; i < 3; i++) {
            Thread thread = new MyThread();
            thread.setNAme(i + "번째 쓰레드");
            if (i == 9) thread.setPriority(10);
            thread.start();
        }
    }
}
```

결과를 살펴보면 마지막 쓰레드의 경우 가장 높은 우선순위를 가지도록 설정했습니다.
다만 주의해야 할 점은 쓰레드는 실제로 실행되기 전에 일정 시간의 준비 과정(메모리의 할당 등)이 필요하다는 것을 인지해서 지연시간을 늘리는 것을 고려해야 합니다.


### 쓰레드의 데몬 설정
일반적으로 쓰레드 객체를 실행하면 다른 쓰레드의 종료 여부와 관계없이 자신의 쓰레드가 종료될 때까지 계속 실행됩니다.
따라서 만일 실행된 쓰레드가 무한 반복 쓰레드라면 해당 프로세스는 영원히 종료되지 않을 것입니다.

하지만 해당 쓰레드를 생성해 실행한 주 쓰레드를 포함해 다른 쓰레드가 종료되면 남아 있는 작업이 있다 하더라도 종료해야 할 때가 있습니다.
예를 들면 문서 편집 프로그램에 일정 시간 간격으로 자동 저장을 수행하는 쓰레드가 수행되고 있을 때 문서 편집 프로그램 자체가 종료되면 자동 저장 쓰레드는 더이상 동작할 필요가 없을 것입니다.
이렇게 다른 쓰레드, 정확히는 일반 쓰레드가 모두 종료되면 함께 종료되는 쓰레드를 `데몬 쓰레드(daemon thread)`라고 합니다.

> 여기서는 데몬 쓰레드가 아닌 쓰레드(non-daemon thread)를 편의상 `일반 쓰레드`라고 부르겠습니다.

![daemon thread](asset/daemon_thread.png)

쓰레드의 데몬 설정은 Thread 클래스의 인스턴스 메서드인 setDaemon() 메서드를 사용하며, 기본값은 false입니다.

```java
// 데몬 쓰레드 설정
void setDaemon(boolean on)
```

생성한 객체의 데몬 설정 여부는 Thread 클래스의 인스턴스 메서드인 isDaemon() 메서드를 이용해 언제든지 확인할 수 있습니다.

```java
// 데몬 쓰레드 설정 확인
boolean isDaemon()
```

이때 주의해야 할 점은 데몬 설정은 반드시 쓰레드를 실행하기 전, 즉 start() 메서드 호출 전에 설정해야 한다는 것입니다.
일단 쓰레드가 실행되고 나면 데몬 설정은 바꿀 수 없습니다.

다음은 3.5초 동안 지속되는 main 쓰레드 내에서 5초 동안 지속하는 MyThread 객체를 생성 및 실행한 예입니다.
여기서 MyThread는 일반 쓰레드로 정의했습니다.
결과를 살펴보면 프로그램이 시작된 지 3.5초 후 main 쓰레드가 종료되어도 MyThread는 자신의 실행이 끝날 때까지 계속 지속되는 것을 알 수 있습니다.

```java
package sec03_threadproperties.EX03_ThreadProperties_3_1;

class MyThread extends Thread {
    @Overried
    public void run() {
        System.out.println(getName() + ": " + (isDaemon()? "데몬 쓰레드":"일반 쓰레드"));
        for (int i = 0; i < 6; i++) {
            System.out.println(getName() + ": " + i + "초");
            try {Thread.sleep(1000);} catch (InterruptedException e) {}
        }
    }
}

public class ThreadProperties_3_1 {
    public static void main(String[] args) {

        // 일반 쓰레드
        Thread thread1 = new MyThread();
        thread1.setDaemon(false);
        thread1.setName("thread1");
        thread1.start();

        // 3.5초 후 main 쓰레드 종료
        try {Thread.sleep(3500);} catch (InterruptedException e) {}
        System.out.println("main Thread 종료");
    }
}
```

output
```
thread1: 일반 쓰레드
thread1: 0초
thread1: 1초
thread1: 2초
thread1: 3초
main Thread 종료
thread1: 4초
thread1: 5초
```

다음은 위의 예제와 동일한 조건으로 생선 한 MyThread 객체를 실행하기 전에 setDaemon(ture)로 설정해 데몬 쓰레드로 정의한 것만 다릅니다.
실행 결과를 살펴보면 MyThread가 아직 실행할 내용이 남아 있는데도 main쓰레드가 종료되면 함께 종료됩니다.

```java
package sec03_threadproperties.EX04_ThreadProperties_3_2;

class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println(getName() + ": " +(isDaemin()? "데몬 쓰레드":"일반 쓰레드"));
        for (int i = 0; i < 6; i++) {
            System.out.println(getName() + ": " + i + "초");
            try {Thread.sleep(1000);} catch (InterruptedException e) {}
        }
    }
}

public class ThreadProperties_3_2 {
    public static void main(String[] args) {

        // 데몬 쓰레드
        Thread thread2 = new MyThread();
        thread2.setDaemon(true);
        thread2.setName("thread2");
        thread2.start();

        // 3.5초 후 main 쓰레드 종료
        try {Thread.sleep(3500);} catch (InterruptedException e) {}
        System.out.println("main Thread 종료");
    }
}
```

output
```
thread2: 데몬 쓰레드
thread2: 0초
thread2: 1초
thread2: 2초
thread2: 3초
main thread 종료
```

다음 예제는 주의를 기울여 살펴볼 필요가 있습니다.
main 쓰레드에서는 MyThread 객체를 2개 생성해 실행했습니다.
이때 첫 번째는 일반 쓰레드, 두 번째는 데몬 쓰레드로 지정했습니다.
즉, 이 예제의 핵심은 `두 번째 데몬 쓰레드가 자신을 실행한 main 쓰레드가 종료되는 3.5초 시점에 종료될 것인가?`하는 것입니다.

```java
package sec03_threadproperties.EX05_ThreadProperties_3_3;

class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println(getName() + ": " + (isDaemon()? "데몬 쓰레드":"일반 쓰레드"));
        for (int i = 0; i < 6; i++) {
            System.out.println(getName() + ": " + i + "초");
            try {Thread.sleep(1000);} catch (InterruptedException e) {}
        }
    }
}

public class ThreadProperties_3_3 {
    public static void main(String[] args) {

        // 일반 쓰레드
        Thread thread1 = new MyThread();
        thread1.setDaemon(false);
        thread1.setName("thread1");
        thread1.start();

        // 데몬 쓰레드
        Thread thread2 = new MyThread();
        thread2.setDaemon(true);
        thread2.setName("thread2");
        thread2.start();

        // 3.5초 후 main 쓰레드 종료
        try {Thread.sleep(3500);} catch (InterruptedException e) {}
        Ststem.out.println("main Thread 종료");
    }
}
```

결과를 살펴보면 두 번째 쓰레드(thread2)는 데몬 쓰레드인데도 main쓰레드가 끝난 이후에도 계속 지속된다는 것을 알 수 있습니다.
대부분 데몬 쓰레드는 자신을 호출한 주 쓰레드가 종료되면 함께 종료된다고 이해할 때가 많습니다.
하지만 데몬 쓰레드는 주 쓰레드가 아니라 프로세스 내의 모든 일반 쓰레드가 종료되어야지만 종료되는 것을 기억해야 합니다.

## 쓰레드의 동기화

### 동기화의 개념

### 동기화의 필요성

### 동기화 방법

### 동기화의 원리


## 쓰레드의 상태

### 쓰레드의 6가지 상태

### NEW, RUNNABLE, TERMINATED

### TIMED_WAITING

### BLOCKED

### WAITING
