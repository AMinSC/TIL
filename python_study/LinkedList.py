class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init
        self.count = 0 # data count

    def __iter__(self):
        currentNode = self.head
        currentNode = currentNode.next
        while currentNode:
            yield currentNode.data
            currentNode = currentNode.next

    def __len__(self):
        return self.count

    def __str__(self):
        s = ''
        currentNode = self.head
        currentNode = currentNode.next
        for i in range(self.count):
            s += f'{str(currentNode.data)}, '
            currentNode = currentNode.next
        return f'<{s[:-2]}>'
        
    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def pop(self):
        lastValue = self.tail.data
        current = self.head
        for i in range(self.count):
            if current.next is self.tail:
                self.tail = current
                break
            current = current.next
        self.count -= 1
        return lastValue

    def find(self, data):
        index = -1
        currentNode = self.head
        for i in range(self.count):
            if currentNode.data == data:
                return index
            index += 1
            currentNode = currentNode.next
        return -1  # 찾지 못했을 때 -1 이 반환 될 수 있는 법 고민

    def get(self, get_idx: int):
        if isinstance(get_idx, int):
            current_node = self.head.next
            if get_idx > self.count - 1:
                raise IndexError('LinkedList index out of range')
            elif get_idx < 0:
                raise IndexError('index 값이 너무 작습니다. 0 이상으로 해주세요.')
            else:
                for i in range(get_idx):
                    current_node = current_node.next
                return current_node.data

    def shift(self):
        self.head.next = self.head.next.next
        self.count -= 1

    def unshift(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def insert(self, idx: int, data):
        if isinstance(idx, int):
            new_node = Node(data)
            current_node = self.head.next
            if idx > self.count - 1:
                raise IndexError('LinkedList index out of range')
            elif idx < 0:
                raise IndexError('index 값이 너무 작습니다. 0 이상으로 해주세요.')
            else:
                for i in range(idx - 1):
                    current_node = current_node.next
                self.count += 1
                new_node.next = current_node.next
                current_node.next = new_node
                print(current_node.data, new_node.next.data, new_node.data)
    
    def delete(self, idx: int):
        if isinstance(idx, int):
            current_node = self.head.next
            if idx > self.count - 1:
                raise IndexError('LinkedList index out of range')
            elif idx < 0:
                raise IndexError('index 값이 너무 작습니다. 0 이상으로 해주세요.')
            else:
                for i in range(idx - 1):
                    current_node = current_node.next
                current_node.next = current_node.next.next
                self.count -= 1
