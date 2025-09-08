from collections import defaultdict

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.topindex = -1
        self.minVal = defaultdict(int)

    def push(self, val):
        self.stack.append(val)
        self.topindex = len(self.stack) - 1
        if self.topindex == 0:
            self.minVal[self.topindex] = val
        else:
            self.minVal[self.topindex] = min(self.minVal[self.topindex - 1], val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.topindex = len(self.stack) - 1

    def top(self):
        return self.stack[self.topindex]

    def getMin(self):
        return self.minVal[self.topindex]


# ---------------- 本地驱动测试 ----------------
if __name__ == "__main__":
    ops = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    params = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

    obj = None
    results = []

    for op, p in zip(ops, params):
        if op == "MinStack":
            obj = MinStack()
            results.append(None)
        elif op == "push":
            obj.push(p[0])
            results.append(None)
        elif op == "pop":
            obj.pop()
            results.append(None)
        elif op == "top":
            results.append(obj.top())
        elif op == "getMin":
            results.append(obj.getMin())

        print(results)
