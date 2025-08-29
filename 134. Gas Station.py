class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                # 从 start 到 i 都不行，起点跳到 i+1
                start = i + 1
                tank = 0

        return start if total >= 0 and start < len(gas) else -1
