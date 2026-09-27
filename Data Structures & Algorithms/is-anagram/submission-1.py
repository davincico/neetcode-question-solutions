class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # must have same length
        # same count of same letters, position dont matter
        s = sorted(s.replace(" ", "").lower())
        t = sorted(t.replace(" ", "").lower())
        return s == t