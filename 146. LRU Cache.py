class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.od=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key,last=False)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key]=value
            self.od.move_to_end(key,last=False)
        else:
            self.od[key]=value
            self.od.move_to_end(key,last=False)
            if len(self.od)>self.cap:
                self.od.popitem(last=True)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)