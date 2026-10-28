class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.n = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val == -1:
            return val
        for k in self.cache:
            if k == key:
                self.cache[k][1] = 0
            else:
                self.cache[k][1] += 1
        
        return val[0]

    def put(self, key: int, value: int) -> None:
        if not self.cache.get(key, 0) and len(self.cache) == self.cap:
            lru = None
            m = -1
            for k in self.cache:
                if self.cache[k][1] > m:
                    lru = k
                    m = self.cache[k][1]
            
            del self.cache[lru]

        for k in self.cache:
            self.cache[k][1] += 1

        self.cache[key] = [value, 0]
