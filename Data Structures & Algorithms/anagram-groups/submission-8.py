# Hash Table
"""

1. Represent each string by frequency of characters
- lowercase array of length 26 (a-z)
- anagrams must have identical frequency arrays
- freq array converted to a tuple to be dictionary key (immutable)
2. Append string to list associated with key
3. Return list stored 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} 
        for string in strs:
            count = [0] * 26 # initial array of all 0s
            for char in string:
                # ord('a') = 97
                # ord('b') = 98
                # so ord(char) - ord('a') gives index 0-25
                index = ord(char) - ord('a') # index of char in 0-25
                count[index] += 1  # counter at position of char
            
            # Convert list to tuple to use as dict key (must be immutable)
            hashmap_key = tuple(count)
            if hashmap_key not in res:
                res[hashmap_key] = []
            res[hashmap_key].append(string)
        return list(res.values())
                
        