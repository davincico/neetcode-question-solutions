class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Use two pointers, start end and move inwards
        - skip any non-letter/digit characters
        - compare in lowercase
        - if not same, non palindrome
        """
        # isalnum() return True/False, use it as a check
        left = 0 # first
        right = len(s) - 1 # last

        while left < right:
            # moves down the string inwards until alpha/digit found
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False # disqualify when no match
            # Now continue down the string inwards as long as left < right
            left +=1
            right -=1
        return True # ONLY reach the end if no mismatch
            




