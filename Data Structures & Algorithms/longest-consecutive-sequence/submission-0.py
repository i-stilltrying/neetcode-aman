class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        for num in nums:
            count=1
            next_num=num+1
            while(next_num in nums):
                count+=1
                next_num+=1
            longest= max(longest,count)
        return longest