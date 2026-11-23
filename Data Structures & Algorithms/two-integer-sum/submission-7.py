class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for n in range(len(nums)):
            for i in range(n+1, len(nums)):
                total = nums[n] + nums[i]
                if total == target:
                    result.append(n)
                    result.append(i)
                    return result
        return result