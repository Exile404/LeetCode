class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        result = []
        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                result.append(total_product // num)
        return result
