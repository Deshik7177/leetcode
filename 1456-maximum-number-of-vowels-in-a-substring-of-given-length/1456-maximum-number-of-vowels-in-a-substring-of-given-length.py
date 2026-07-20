class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_count=0
        for i in range(k):
            if s[i] in "aeiou":
                window_count += 1
        max_count = window_count
        for i in range(len(s)-k):
            if s[i] in "aeiou":
                window_count -= 1
            if s[i+k] in "aeiou":
                window_count +=1
            max_count = max(window_count,max_count)
        return max_count