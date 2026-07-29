class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)< sum(cost):
            return -1
        stations = len(gas)
        tank = 0
        start = 0
        for i in range(stations):
            tank = tank - cost[i] + gas[i]
            
            if tank < 0:
                start = i + 1
                tank = 0
            
        return start