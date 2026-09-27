class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t): # To be Anagram must be same length
            return False
        countofs, countoft = {}, {}
        """ First build the hashmap
            1) if s = "aab", len=3, i = [0,1,2]
            i=0, s[i] = "a"
            - now access dictionary countofs using "a" as the key
            - "a" does not exist yet, so .get(s[1],0) returns 0
            - creates key of "a" with value 1
        """
        for i in range(len(s)): 
            countofs[s[i]] = 1 + countofs.get(s[i], 0) 
            countoft[t[i]] = 1 + countoft.get(t[i], 0)
        return countofs == countoft