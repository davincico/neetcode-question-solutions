class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = 0
        maxi = 0
        for i in nums:
            if i ==1:
                counts +=1
            elif i ==0:
                maxi = max(counts, maxi)
                counts = 0
        return max(maxi, counts)

