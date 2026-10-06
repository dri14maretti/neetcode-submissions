class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        readNode = self.cache[key]

        self._remove(readNode)
        self._insert(readNode)

        return readNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self.count -= 1
        
        newNode = Node(value, key)

        self.cache[key] = newNode
        self._insert(newNode)

        self.count +=1

        if self.count > self.capacity:
            lru = self.head.next
            self._remove(lru)
            self.cache.pop(lru.key)
            self.count -= 1

    def _remove(self, node):
        next = node.next
        prev = node.prev

        next.prev = prev
        prev.next = next

    def _insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

