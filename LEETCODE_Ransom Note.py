class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        me = list(magazine)
        for i in ransomNote:
            if i not in me:
                return False
            me.remove(i)
        return True
