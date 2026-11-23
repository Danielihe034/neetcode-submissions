class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for num in range(len(nums)):
            if nums[num] in hs:
                return True
            else:
                hs.add(nums[num])
        return False
            