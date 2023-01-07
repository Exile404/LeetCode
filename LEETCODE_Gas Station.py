class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        store = 0
        index = 0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(cost)):
            store+=(gas[i]-cost[i])
            if store < 0:
                store = 0
                index = i+1
        return index
