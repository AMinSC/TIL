
- 알고리즘 풀이에서 `input()` 함수를 사용하여 `시간 초과`가 발생될 경우 `sys.stdin.readline()` 함수로 해결할 수 있습니다.
    ```python
    >>> import sys
    >>> sys.stdin.readline()
    hello, world!!
    'hello, world!!\n'
    ```
    - input() 함수는 사용자 입력을 받을 때 prompt message를 출력하고, 입력 값을 문자열로 변환한 후 개행 문자를 제거하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않고, 개행 문자를 포함하여 입력 값을 한 번에 버퍼로 읽어들입니다.
    - readline을 호출하면 포인터는 \n 문자에 도달할 때까지 읽고, 방금 지나간 부분을 사용자에게 반환한 후 제자리에 머물면서 사용자가 다시 포인터를 움직일 때까지 기다립니다. readline을 다시 호출하면 포인터가 다음 \n이 있을 때까지 이동하고, 그렇지 않으면 EOF가 발생합니다.
    - 따라서 sys.stdin.readline()을 사용하면 입력 속도가 개선되며, 특히 대량의 입력을 처리할 때 유용

---
