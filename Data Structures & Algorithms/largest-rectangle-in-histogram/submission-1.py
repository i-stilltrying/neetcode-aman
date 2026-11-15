class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:

        rightstack=[]
        rightresult=[len(height)]*len(height)
        for i in range(len(height)-1,-1,-1):
            while rightstack and height[rightstack[-1]]>=height[i]:
                rightstack.pop()
            if rightstack:
                rightresult[i] = rightstack[-1]
            rightstack.append(i)

        leftstack=[]
        leftresult=[-1]*len(height)
        for i in range(len(height)):
            while leftstack and height[leftstack[-1]]>=height[i]:
                leftstack.pop()
            if leftstack:
                leftresult[i] = leftstack[-1]
            leftstack.append(i)

        maxarea = 0
        for i in range(len(height)):
            curr = (rightresult[i] - leftresult[i] - 1) * height[i]
            maxarea = max(curr, maxarea)
        return maxarea


