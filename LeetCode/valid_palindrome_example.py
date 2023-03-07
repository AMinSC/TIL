import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)

        if s == s[::-1]:
            print("True")
        else:
            print("False")
