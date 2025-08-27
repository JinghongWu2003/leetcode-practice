import random

class RandomizedSet(object):
    def __init__(self):
        self.arr = []      # 存元素，支持随机下标
        self.pos = {}      # val -> index in arr

    def insert(self, val):
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val):
        if val not in self.pos:
            return False
        i = self.pos[val]
        last = self.arr[-1]
        # 把最后一个元素搬到 i 位置，填补空洞
        self.arr[i] = last
        self.pos[last] = i
        # 删掉末尾与哈希表记录
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        return random.choice(self.arr)
