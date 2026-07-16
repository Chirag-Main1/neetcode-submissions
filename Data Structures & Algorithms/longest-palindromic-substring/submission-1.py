# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         res = ''
#         for i in range(n):
#             a = ''
#             for j in s[i:]:
#                 a += j
#                 if a == a[::-1]:
#                     if len(a)>len(res):
#                         res = a
                
#         return res

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            # left and right are now one step outside the palindrome
            return s[left + 1:right]

        for i in range(n):
            # Odd length palindrome
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(res):
                res = odd

            if len(even) > len(res):
                res = even

        return res