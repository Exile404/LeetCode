class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = [["(",1,0]]
        while len(stack)!=0:
            s,left,right = stack.pop()
            if len(s)==2*n:
                ans.append(s)
            if left<n:
                stack.append([s+"(",left+1,right])
            if right<left:
                stack.append([s+")",left,right+1])
        return ans
