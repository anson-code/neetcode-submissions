class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        seen = set()

        res = 0

        for num in nums:
            if num in seen:
                continue
            temp = num
            seen.add(num)
            while temp in hashset:
                seen.add(temp)
                temp += 1
            res = max(res,(temp-num))
        
        return res
                

