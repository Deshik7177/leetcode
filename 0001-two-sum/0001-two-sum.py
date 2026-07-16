class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index, value in enumerate(nums):
            x=target - value
            if x in dict:
                return index, dict[x]
            else:
                dict[value]=index
