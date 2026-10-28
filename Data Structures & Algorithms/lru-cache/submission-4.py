class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val = key, val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        prev, nxt = self.head, self.head.next
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
