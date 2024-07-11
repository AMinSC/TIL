import threading


class SynchronizedList:
    def __init__(self):
        self.list = []
        self.lock = threading.Lock()

    def append(self, item):
        with self.lock:
            self.list.append(item)

    def __str__(self):
        return str(self.list)


if __name__ == "__main__":
    sync_list = SynchronizedList()
    sync_list.append(1)
    sync_list.append(2)
    print(sync_list)