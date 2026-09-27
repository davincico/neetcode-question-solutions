class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Clean and reverse, compare reversed and original
        """
        cleaned = ""
        # Build only letters and digits
        for char in s:
            if char.isalnum(): 
                cleaned += char.lower() # add lowercase
        return cleaned == cleaned[::-1] 