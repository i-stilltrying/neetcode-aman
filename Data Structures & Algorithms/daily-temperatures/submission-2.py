class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        result=[-1]*len(t)
        stack=[]
        for i in range(len(t)-1,-1,-1):
            while stack and t[stack[-1]]<=t[i]:
                stack.pop()
            if stack:
                result[i]=stack[-1]
            stack.append(i)
        for i in range(len(t)):
            result[i] = result[i] - i if result[i] != -1 else 0

        return result