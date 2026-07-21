class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        left = 0
        right = 0
        length = float("inf")
        while right != len(nums):
            if curr_sum < target:
                curr_sum += nums[right]
                right+=1
            while curr_sum >= target:
                length = min(length,right-left)
                curr_sum -= nums[left]
                left+=1
        if length == float("inf"):
            return 0
        else:
            return length