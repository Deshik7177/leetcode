class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        count=0
        for i in range(len(s)):
            if s[i]=='L':
                bal+=1
            elif s[i]=='R':
                bal-=1
            if bal==0:
                count+=1
        return count