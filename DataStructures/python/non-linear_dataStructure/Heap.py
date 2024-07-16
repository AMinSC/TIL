import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.push(10)
    min_heap.push(5)
    min_heap.push(20)

    print(min_heap.pop())
    print(min_heap.peek())