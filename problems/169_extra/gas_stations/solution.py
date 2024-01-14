class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [0] * n
        for i in range(n):
            diff[i] = gas[i] - cost[i]
        print(diff)

        tot = 0
        start = 0
        for i in range(n):
            tot += diff[i]
            if tot < 0:
                tot = 0
                start = i+1
        for i in range(n):
            if i == start:
                return start

            tot += diff[i]
            if tot < 0:
                return -1
        return -1