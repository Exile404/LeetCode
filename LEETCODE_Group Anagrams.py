class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x not in store:
                store[x] = [i]
            else:
                store[x].append(i)
        l = []
        for k,v in store.items():
            l.append(v)
        return l
