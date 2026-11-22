# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev=dummy
        while True:
            kth=self.getkth(groupPrev,k)
            if kth==None:
                break
            groupnext=kth.next

            prev=kth.next
            curr=groupPrev.next
            while curr!=groupnext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            newgroupPrev=groupPrev.next
            groupPrev.next=kth
            groupPrev=newgroupPrev
        return dummy.next
            
    def getkth(self, curr, k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
        