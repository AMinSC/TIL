import threading


class SynchronizedDict:
    def __init__(self):
        self.dict = {}
        self.lock = threading.Lock()

    def __setitem__(self, key, value):
        with self.lock:
            self.dict[key] = value

    def __getitem__(self, key):
        with self.lock:
            return self.dict[key]

    def __str__(self):
        with self.lock:
            return str(self.dict)


if __name__ == "__main__":
    sync_dict = SynchronizedDict()
    sync_dict['key1'] = 'value1'
    print(sync_dict)
