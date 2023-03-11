class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
    
        for num in nums:
            new_perms = []
            for perm in result:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [num] + perm[i:])
            result = new_perms
        return result
