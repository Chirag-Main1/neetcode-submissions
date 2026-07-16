# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         res = []
#         for i in range(n):
#             a = ''
#             for j in s[i:]:
#                 a += j
#                 if a == a[::-1]:
#                         res.append(a)
                
#         return len(res)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = []

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                res.append(s[left:right + 1])
                left -= 1
                right += 1

        for i in range(n):
            # Odd length palindrome
            expand(i, i)

            # Even length palindrome
            expand(i, i + 1)

        return len(res)