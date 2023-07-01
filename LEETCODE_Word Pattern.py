class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i, c in enumerate(pattern):
            if c not in char_to_word:
                if words[i] in word_to_char:
                    return False
                char_to_word[c] = words[i]
                word_to_char[words[i]] = c
            else:
                if char_to_word[c] != words[i]:
                    return False

        return True
            
