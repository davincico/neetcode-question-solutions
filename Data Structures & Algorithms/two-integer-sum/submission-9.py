class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # 1. Fill the hashmap with index and value from array
        for index, value in enumerate(nums):
            # you get index and value 0 2, 1 7 etc
            hashmap[value] = index # if using index as the key to the dict --> {0:2, 1:7 ..}
        # 2. Check if diff exist in hashmap
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap and hashmap[diff] != index : # search value == diff AND the index should not use the same position
                return [index, hashmap[diff]]