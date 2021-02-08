class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cmp = 0
        for i in range(len(nums)):
            for j in range (len(nums)):
                if nums[i] == nums[j] and i < j:
                    cmp+=1
                else:
                    continue
        return cmp