class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = {}
        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        sum = 0
        for k,v in dic.items():
            if dic[k] == 1:
                return -1
            if dic[k]>=2:
                if dic[k] == 2:
                    sum += 1
                elif dic[k] % 3 == 0:
                    sum += (dic[k] // 3)
                else:
                    sum += ((dic[k] // 3) + 1)
        return sum
        
