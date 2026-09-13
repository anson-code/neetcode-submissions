class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        res = 0

        for num in nums:
            if num - 1 not in hashset:
                temp = num + 1
                while temp in hashset:
                    temp += 1
                res = max(res,temp-num)

        return res


