class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = ""
        n = min(len(word1),len(word2))
        for i in range(n):
            arr += word1[i]
            arr += word2[i]
        if n==len(word1):
            arr += word2[n:]
        elif n==len(word2):
            arr += word1[n:]
        return arr