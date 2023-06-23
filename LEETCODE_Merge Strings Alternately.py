class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        merged = ""

        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1 < len(word1):
                merged += word1[ptr1]
                ptr1 += 1
            if ptr2 < len(word2):
                merged += word2[ptr2]
                ptr2 += 1

        return merged
