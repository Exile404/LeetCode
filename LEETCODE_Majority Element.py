class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        return max(dic, key=dic.get)
