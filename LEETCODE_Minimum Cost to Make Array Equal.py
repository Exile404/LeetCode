class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_value(num):
            res = 0
            for i in range(len(nums)):
                res+=abs(num-nums[i])*cost[i]
            return res
        l, r =min(nums),max(nums)
        ans = get_value(nums[0])
        while l<r:
            mid = (l+r)//2
            ans1 = get_value(mid)
            ans2 = get_value(mid+1)
            ans = min(ans1,ans2)
            if ans1>ans2:
                l = mid+1
            else:
                r = mid
        return ans
