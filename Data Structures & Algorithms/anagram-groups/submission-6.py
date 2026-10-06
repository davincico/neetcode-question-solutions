# 1. Sorting and Match
"""
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

1. Create hashmap where key is sorted version of string, value is list of strings in anagram group. 
- hashmap = { sorted_string : ["string_a", "string_b"]}
2. Iterate through each string in input list
- sort char to form key
- append original string to list : sorted_key
3. Return all values only of hashmap
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams become identical when sorted (same frequency of same char)
        res = {} # hashmap initialize
        for string in strs:
            sorted_string = ''.join(sorted(string)) # sorted(string) gives list of sorted char, have to join back to get sorted string
            if sorted_string not in res:
                res[sorted_string] = []
            res[sorted_string].append(string)
        return list(res.values())
                    


