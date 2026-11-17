class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        a,b=num1,num2
        total=len(num1)+len(num2)
        half=total//2

        if len(b)<len(a):
            a,b=b,a
        l=0
        r=len(a)-1
        while True:
            ma=(l+r)//2
            mb=half-ma-2

            aleft=a[ma]    if ma >= 0 else float("-infinity")     
            aright=a[ma+1] if (ma + 1) < len(a) else float("infinity")
            bleft=b[mb]    if mb >= 0 else float("-infinity")
            bright=b[mb+1] if (mb + 1) < len(b) else float("infinity")

            if aleft<=bright and bleft<=aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = ma - 1
            else:
                l = ma + 1

        