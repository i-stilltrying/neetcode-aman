class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        result=[]
        nums.sort()
        r=n-1
        l=0
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            fixed=nums[i]
            target=-fixed
            r=n-1
            l=i+1
            while( l<r):
                current_sum = nums[l] + nums[r]
                if current_sum==target:
                    result.append([fixed,nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1

                elif current_sum>target: r-=1
                else: l+=1
        return result
        



