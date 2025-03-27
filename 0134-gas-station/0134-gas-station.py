class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:
            return -1

        tank = 0
        start = -1
        
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
             # If tank goes negative, reset start position
            if tank < 0:
                start = i + 1
                tank = 0

        return start