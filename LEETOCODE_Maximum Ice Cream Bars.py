class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        store = 0
        for i in costs:
            if i>coins:
                break
            else:
                coins -=i
                store+=1
        return store
