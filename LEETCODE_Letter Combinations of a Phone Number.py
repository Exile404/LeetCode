class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
        '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        combinations = []
        if digits == "":
            return []
        def dfs(index, combination):
            
            if index == len(digits):
                combinations.append(combination)
                return
           
            letters = numpad[digits[index]]
            
            for letter in letters:
                dfs(index + 1, combination + letter)
        dfs(0, '')
        
        return combinations
