def longestCommonPrefix(strs):
    s1 = ''
    s = strs[0]
    k=0
    for i in range(len(s)):
        match = s[:k + 1]
        c = 1
        for j in range(1, len(strs)):
            s2=strs[j]
            if match == s2[:k+1]:
                c += 1

        if c == len(strs):
            s1=match
        k+=1
    return s1

strs = ["flower","flow","flood"]
print(longestCommonPrefix(strs))
