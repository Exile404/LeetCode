def parentheses(s):
    l=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            l.append(s[i])
        else:
            if len(l)==0:
                return False
            x=l[-1]
            if x=='(' and s[i]==')':
                l.pop()
            elif x=='{' and s[i]=='}':
                l.pop()
            elif x=='[' and s[i]==']':
                l.pop()
            else:
                return False
    if len(l)!=0:
        return False
    return True
s=input()
print(parentheses(s))