import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0] if self.heap else None


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push((2, "task2"))
    pq.push((1, "task1"))
    pq.push((3, "task3"))

    print(pq.pop())
    print(pq.peek())