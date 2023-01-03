class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        num.sort()
        x = len(num)
        if x%2==0:
            c = (num[(x//2)-1]+num[x//2])/2
        else:
            c = num[(x//2)]
        c = round(c,5)
        return c
        
