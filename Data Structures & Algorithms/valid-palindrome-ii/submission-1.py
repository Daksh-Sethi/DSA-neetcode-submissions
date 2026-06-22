class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        n = len(s)
        right = n-1
        delch = False
        while(left<right):
            if not s[left].isalnum():
                left = left +1
                continue
            if not s[right].isalnum():
                right = right -1
                continue
            if s[left].lower() != s[right].lower():
                if delch == False:
                    if s[left].lower() == s[right-1].lower():
                        right = right -1
                        delch = True
                        continue
                    elif s[left +1].lower() == s[right].lower():
                        left = left +1
                        delch = True
                        continue
                    else:
                        return False
                return False
            left = left +1 
            right = right -1
        return True
            