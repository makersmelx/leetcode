class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        ret = float("inf")
        cur = nums[0]
        
        while left <= right and right < len(nums):
            if cur < target:
                right += 1
                if right >= len(nums):
                    break
                cur += nums[right]
            else:
                ret = min(ret, right - left + 1)
                cur -= nums[left]
                left += 1
        
        return 0 if ret == float('inf') else ret
                