class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # 3,4,5
            for j in range(i+1, len(nums)): # moving 1 ahead
                if nums[i] + nums[j] == target: # 3 + 4 == 7, nums[0] + nums[1]
                    return [i,j]
            


