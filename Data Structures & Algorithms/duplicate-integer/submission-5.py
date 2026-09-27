class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # sorted to be adjacent
        for i in range(len(nums)-1): # range(5) gives 0,1,2,3,4, stop 1 earlier as nums[i+1] will hit it
            if nums[i] == nums[i+1]:
                return True
        return False