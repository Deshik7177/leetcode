class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for i in nums:
            if i:
                count+=1
            else:
                count=0
            if count > maxi:
                maxi = count
        return maxi