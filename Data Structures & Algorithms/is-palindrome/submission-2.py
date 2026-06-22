class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        left = 0
        right = n-1
        while(left<right):
            if not (s[left].isalnum()):
                left = left+1
                continue
            if not (s[right].isalnum()):
                right = right -1
                continue
            if(s[left].lower()!=s[right].lower()):
                return False
            left = left + 1
            right = right -1
        return True