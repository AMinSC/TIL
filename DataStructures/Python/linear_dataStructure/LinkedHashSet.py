from collections import OrderedDict


class LinkedHashSet:
    def __init__(self):
        self.set = OrderedDict()

    def add(self, item):
        self.set[item] = None

    def __str__(self):
        return str(list(self.set.keys()))


if __name__ == "__main__":
    linked_hash_set = LinkedHashSet()
    linked_hash_set.add(1)
    linked_hash_set.add(2)
    linked_hash_set.add(1)
    print(linked_hash_set)