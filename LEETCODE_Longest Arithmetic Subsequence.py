class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_length = 0

        for i in range(len(nums)):
            dp[i] = {}

            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

                max_length = max(max_length, dp[i][diff])

        return max_length
