class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        fact = [1]
        for i in range(1,n):
            fact.append(fact[-1]*i)
        k = k-1
        res = ''
        for i in range(n,0,-1):
            idx = k//fact[i-1]
            res+=str(nums[idx])
            nums.pop(idx)
            k = k%fact[i-1]
        return res
        
