class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # counter with forward move
        res = 0 
        for i in range(len(nums)): # len=3, range = 0,1,2 positions
            count = 0
            for j in range(i, len(nums)): # start from i, i+1, i+2
                if nums[j] == 0:
                    break
                count += 1
            res = max (res, count) # keeps the max found between 2 numbers
        return res