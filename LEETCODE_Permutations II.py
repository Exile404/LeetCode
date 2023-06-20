class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
    
        for num in nums:
            new_perms = []
            for perm in result:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [num] + perm[i:])
            result = new_perms
        ans = []
        for i in result:
            if i not in ans:
                ans.append(i)
        return ans
