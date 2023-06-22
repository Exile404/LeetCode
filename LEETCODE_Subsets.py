class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        store = []
        total_combinations = 2 ** n

        for i in range(total_combinations):
            l = []
            for j in range(n):
                if (i >> j) & 1:
                    l.append(nums[j])
            store.append(l)

        return store
