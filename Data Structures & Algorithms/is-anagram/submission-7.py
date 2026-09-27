class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) == len(t): # To be Anagram must be same length
            countofs, countoft = {}, {}
            # Loop to count occurence of char in each string
            for i in range(len(s)): # 0, 1, 2, - i can be index for both strings since same legnth
                countofs[s[i]] = 1 + countofs.get(s[i], 0) # .get handles keyerror if key dont exist, give default value of 0
                countoft[t[i]] = 1 + countoft.get(t[i], 0)
            for c in countofs:
                if countofs[c] != countoft.get(c,0): # Should LOOP all the way until cleared
                    return False
            return True
        else:
            return False