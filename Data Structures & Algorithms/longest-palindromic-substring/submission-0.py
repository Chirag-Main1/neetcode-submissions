class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            a = ''
            for j in s[i:]:
                a += j
                if a == a[::-1]:
                    if len(a)>len(res):
                        res = a
                
        return res
