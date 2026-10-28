class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            heapq.heappush(self.store[key], (timestamp, value))
            return
        self.store[key] = [(timestamp, value)]
        heapq.heapify(self.store[key])

    def get(self, key: str, timestamp: int) -> str:
        elems = []
        while key in self.store and self.store[key]:
            if timestamp < self.store[key][0][0]:
                break
            
            t, v = heapq.heappop(self.store[key])
            elems.append((t, v))

            if timestamp == t:
                break

        res = ""
        if elems:
            res = elems[-1][1]
        
        # restore
        if key in self.store:
            self.store[key] += elems
            heapq.heapify(self.store[key])
        return res
