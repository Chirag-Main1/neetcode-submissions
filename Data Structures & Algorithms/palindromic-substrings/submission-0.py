class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = []
        for i in range(n):
            a = ''
            for j in s[i:]:
                a += j
                if a == a[::-1]:
                        res.append(a)
                
        return len(res)

