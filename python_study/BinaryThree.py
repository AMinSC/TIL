class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    node_list = []
    def __init__(self, data):
        init = Node(data)
        self.root = init
        self.count = 1
        self.node_list.append(data)

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.node_list)

    def depth(self):
        depth_list = []
        min_depth = min(self.node_list)
        max_depth = max(self.node_list)

        for depth in [min_depth, max_depth]:
            currentNode = self.root
            cnt = 0
            while currentNode:
                if depth == currentNode.data:
                    depth_list.append(cnt)
                    break
                elif depth < currentNode.data:
                    # 왼쪽으로 가야합니다.
                    if not currentNode.left:
                        depth_list.append(cnt)
                        break
                    # 만약 왼쪽 노드가 비어있지 않다면
                    currentNode = currentNode.left
                    cnt += 1
                elif depth > currentNode.data:
                    # 오른쪽으로 가야합니다.
                    if not currentNode.right:
                        depth_list.append(cnt)
                        break
                    # 만약 오른쪽 노드가 비어있지 않다면
                    currentNode = currentNode.right
                    cnt += 1
        return max(depth_list)

    def insert(self, data):
        self.node_list.append(data)
        newNode = Node(data)
        currentNode = self.root

        while currentNode:
            # 같은 값이면 값을 추가시켜주지 않습니다.
            if data == currentNode.data:
                return
            elif data < currentNode.data:
                # 왼쪽으로 가야합니다.
                if not currentNode.left:
                    # 만약 왼쪽 노드가 비어있으면
                    currentNode.left = newNode
                    self.count += 1
                    return
                # 만약 왼쪽 노드가 비어있지 않다면
                currentNode = currentNode.left
            elif data > currentNode.data:
                # 오른쪽으로 가야합니다.
                if not currentNode.right:
                    # 만약 오른쪽 노드가 비어있으면
                    currentNode.right = newNode
                    self.count += 1
                    return
                # 만약 오른쪽 노드가 비어있지 않다면
                currentNode = currentNode.right

    def delete(self, value):
        currentNode = self.root
        self.node_list.remove(value)

        while currentNode:
            if value < currentNode.data:
                if value == currentNode.left.data:
                    # 만약 왼쪽 노드가 찾던 값이면
                    if currentNode.left.left:
                        if currentNode.left.right:
                            currentNode.left.right.left = currentNode.left.left
                            currentNode.left = currentNode.left.right
                        else:
                            currentNode.left = currentNode.left.left
                    else:
                        currentNode.left = None
                    self.count -= 1
                    return
                # 만약 왼쪽 노드가 찾던값이 아니면
                currentNode = currentNode.left
            elif value > currentNode.data:
                if value ==  currentNode.right.data:
                    # 만약 오른쪽 노드가 찾던 값이면
                    if currentNode.right.left:
                        if currentNode.right.right:
                            currentNode.right.right.left = currentNode.right.left
                            currentNode.right = currentNode.right.right
                        else:
                            currentNode.left = currentNode.left.left
                    else:
                        currentNode.right = None
                    self.count -= 1
                    return
                # 만약 오른쪽 노드가 찾던값이 아니면
                currentNode = currentNode.right

    # 깊이 우선 탐색 : 스택
    def DFS(self):
        result = []
        stack = [self.root]

        while len(stack) != 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            result.append(current.data)
        return result

    # 너비 우선 탐색 : 큐
    def BFS(self):
        result = []
        queue = [self.root]

        while len(queue) != 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            result.append(current.data)
        return result


