# input array = [1,2,3,4]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # length of set < length of array = duplicates because set only keeps unique elements
        return len(set(nums)) < len(nums)