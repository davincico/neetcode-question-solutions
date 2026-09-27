class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # len=3, you get 0,1,2,3
            for j in range( i+1, len(nums)): # you want 1,2,3
                if nums[i] + nums[j] == target:
                    return [i, j]